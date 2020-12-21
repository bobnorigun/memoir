from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'blog/index.html')

def result(request):
    a = request.GET['a']
    b = request.GET['b']
    c = int(a) + int(b)
    return render(request, 'blog/result.html', {'c' : c})

#템플릿에서 사용될 context변


#render는 템플릿을 불러오고, redirect는 URL로 이동합니다.
#render(request, template_name, context=None, content_type=None, status=None, using=None)을 파라미터로 가질 수 있다.
#이 중에서 request와 template_name(불러올 html)은 필수.
#context는 딕셔러니형으로 사용하며 key값이 템플릿에서 사용할 변수이름, value값이 파이썬 변수가 됩니다.
