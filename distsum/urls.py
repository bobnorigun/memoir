from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views


app_name = 'distsum'
urlpatterns = [
	path('', views.distsum, name="imhere"),
	path('out/', views.caldistview, name="out"),
]