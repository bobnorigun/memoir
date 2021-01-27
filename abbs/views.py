from django.shortcuts import render
from abbs.models import Genre, Book, PapaAbb
from blog.models import Post

def about(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    # papaabb 내용 추가.
    num_posts = Post.objects.all().count()
    num_abbs = PapaAbb.objects.all().count()
    # book instance와 author 내용은 제외.

    context = {
        'num_posts' : num_posts,
        'num_abbs' : num_abbs,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'about.html', context=context)


# Create your views here.
from django.views import generic

# 호출하는 페이지 링크는 model명이 앞에 붙고 _list 즉, papaabb_list.html임.
class AbbListView(generic.ListView):
    model = PapaAbb
    ordering = ['-created_date']

# 레코드가 없으면 자동으로 404페이지 호출.
class AbbDetailView(generic.DetailView):
    model = PapaAbb
