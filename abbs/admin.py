from django.contrib import admin

# Register your models here.

from .models import Genre, Book, PapaAbb, GetWeb, Comment

admin.site.register(Genre)
admin.site.register(Book)
admin.site.register(PapaAbb)
admin.site.register(GetWeb)
admin.site.register(Comment)

# 어드민도 뷰를 정의해서 어드민페이지에서 디테일한 내용이나 관련 편집도 가능. 그너데 이건 나중에.
