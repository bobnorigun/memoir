from django.urls import path
from . import views

#프로젝트 상위 urls에서 catalog/하위 폴더들을 호출했으니 이제 하위 urls들을 정리.
#path에 정의한 name은 템플릿에서 reverse 매핑하는 링크경로에 해당.
urlpatterns = [
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'), #/는 왜?
    path('book/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
]

# uuid는 bookinstance_id에 해당함. model에서 id를 UUIDField로 만듦. uuid의 primary_key라는 해석.
urlpatterns += [
    path('book/<uuid:pk>/renew/', views.renew_book_librarian, name='renew-book-librarian'),
    path('mybooks/', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
]
