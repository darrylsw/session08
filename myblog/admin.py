from django.contrib import admin
from myblog.models import Post
from myblog.models import Category
from myblog.models import AdminPost
from myblog.models import AdminCategory

# Register your models here.

admin.site.register(Post, AdminPost)
admin.site.register(Category, AdminCategory)
