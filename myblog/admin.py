from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User
from myblog.models import Post
from myblog.models import Category

class CategoriesInline(admin.TabularInline):
    model = Category.posts.through

class AdminPost(admin.ModelAdmin):
    title = models.CharField(max_length=128)
    text = models.TextField(blank=True)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField(blank=True, null=True)
    inlines = [
        CategoriesInline,
    ]

    def __str__(self):
        return self.title

class AdminCategory(admin.ModelAdmin):
    name = models.CharField(max_length=128)
    description = models.TextField(blank=True)
    posts = models.ManyToManyField(Post, blank=True,
                                   related_name='categories')
    inlines = [
        CategoriesInline,
    ]
    exclude = ('category', 'posts')

    def __str__(self):
        return self.name

# Register your models here.

admin.site.register(Post, AdminPost)
admin.site.register(Category, AdminCategory)
