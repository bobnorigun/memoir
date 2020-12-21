from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator #paginator
from django.shortcuts import redirect
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import PPost, CComment, Images
from .forms import PostForm, CommentForm
from django.db.models import Q
from django.db.models import Max

# Create your views here.
def post_list(request):
    post_all = PPost.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    paginator = Paginator(post_all, 7)
    page = request.GET.get('page')
    posts = paginator.get_page(page)
    modified = PPost.objects.annotate(max_activity=Max('last_modified', 'comments__created_date')).order_by('-max_activity')
    return render(request, 'event/post_list.html', {'posts': posts, 'modified': modified})

def post_detail(request, pk):
    post = get_object_or_404(PPost, pk=pk)
    modified = PPost.objects.annotate(max_activity=Max('last_modified', 'comments__created_date')).order_by('-max_activity')
    return render(request, 'event/post_detail.html', {'post': post, 'modified': modified})

def post_event(request):
    context = {"post_event": "active"}
    return render(request, 'event/post_event.html', context)

# pk를 강제로 호출해보자. 265번.
def days(request):
    context = {"days": "active"}
    return render(request, 'event/days.html', context)

def post_recent_list(request):
    modified = PPost.objects.filter(published_date__lte=timezone.now()).order_by('-last_modified')
    return render(request, 'event/post_recent_list.html', {'modified': modified})

@login_required
def post_draft_list(request):
    modified = PPost.objects.annotate(max_activity=Max('last_modified', 'comments__created_date')).order_by('-max_activity')
    posts = PPost.objects.filter(published_date__isnull=True).order_by('-created_date')
    return render(request, 'event/post_draft_list.html', {'posts': posts, 'modified': modified})

@login_required
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            for img in request.FILES.getlist('imgs'):
                photo = Images()
                photo.post = post
                photo.image = img
                photo.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'event/post_edit.html', {'form': form})

@login_required
def post_edit(request, pk):
    post = get_object_or_404(PPost, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'event/post_edit.html', {'form': form})

@login_required
def post_publish(request, pk):
    post = get_object_or_404(PPost, pk=pk)
    post.publish()
    return redirect('post_detail', pk=pk)

@login_required
def post_remove(request, pk):
    post = get_object_or_404(PPost, pk=pk)
    post.delete()
    return redirect('post_list')

def add_comment_to_post(request, pk):
    post = get_object_or_404(PPost, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'event/add_comment_to_post.html', {'form': form})

@login_required
def comment_approve(request, pk):
    comment = get_object_or_404(CComment, pk=pk)
    comment.approve()
    return redirect('post_detail', pk=comment.post.pk)

@login_required
def comment_remove(request, pk):
    comment = get_object_or_404(CComment, pk=pk)
    comment.delete()
    return redirect('post_detail', pk=comment.post.pk)

def post_search(request):
    global paginator

    a = Post.objects.all()
    q = request.GET.get('q','')
    title_q = Q(title__icontains = q)
    text_q = Q(text__icontains = q)
    if q:
        a = a.filter(title_q | text_q).order_by('-published_date')
        paginator = Paginator(a, 7)
    page = request.GET.get('page')
    aas = paginator.get_page(page)
    return render(request, 'event/post_search.html', {'aas':aas, 'q':q})

def result(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return render(request, 'event/result.html', {'c' : c})
