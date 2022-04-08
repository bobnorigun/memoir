from django.contrib import admin
from .models import Post, Comment

admin.site.register(Comment)

#@admin으로 시작하면 list_display이하 옵션을 쓸 수 있음
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'created_date', 'last_modified')
