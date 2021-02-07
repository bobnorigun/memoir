from django.urls import path
from . import views

#프로젝트 상위 urls에서 catalog/하위 폴더들을 호출했으니 이제 하위 urls들을 정리.
#path에 정의한 name은 템플릿에서 reverse 매핑하는 링크경로에 해당.
urlpatterns = [
    path('', views.AbbListView.as_view(), name='index'),
    path('about/', views.about, name='about'),
    path('privacypolicy/', views.privacypolicy, name='privacypolicy'),
    path('abbs/', views.AbbListView.as_view(), name='abbs'), #/는 왜?
    path('abb/<int:pk>', views.AbbDetailView.as_view(), name='abb-detail'),
]

#releasenote Edit
urlpatterns += [
    path('abb/<int:pk>/update/', views.AbbUpdate.as_view(), name='abb-update'),
]
