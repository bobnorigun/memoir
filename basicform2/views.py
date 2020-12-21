from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def result(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return render(request, 'blog/result.html', {'c': c})
    
