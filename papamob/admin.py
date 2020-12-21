from django.contrib import admin
from .models import PPost, CComment, Images

class PhotoInline(admin.TabularInline):
    model = Images

class PostAdmin(admin.ModelAdmin):
    inlines = [PhotoInline, ]

admin.site.register(PPost, PostAdmin)
admin.site.register(CComment)
