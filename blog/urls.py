from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('blog/', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
    path('post/new/', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='post_edit'),
    path('post/<pk>/publish/', views.post_publish, name='post_publish'),
    path('drafts/', views.post_draft_list, name='post_draft_list'),
    path('recent/', views.post_recent_list, name='post_recent_list'),
    path('map/', views.post_map, name='post_map'),
    path('layout/', views.post_layout, name='post_layout'),
    path('app_later/', views.post_app_later, name='post_app_later'),
    path('app_memolang/', views.post_app_memolang, name='post_app_memolang'),
    path('app_nalsilang/', views.post_app_nalsilang, name='post_app_nalsilang'),
    path('post/<pk>/remove/', views.post_remove, name='post_remove'),
    path('post/<int:pk>/comment/', views.add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', views.comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', views.comment_remove, name='comment_remove'),
    path('post/search/', views.post_search, name='post_search'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
