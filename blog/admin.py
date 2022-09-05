from django.contrib.admin.decorators import register
from django.contrib import admin

from .models import Article

@register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status','created_on')
    list_filter = ("status",)
    search_fields = ['title', 'content']
    prepopulated_fields = {'slug': ('title',)}
