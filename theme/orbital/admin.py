from django.contrib import admin
from .models import Category, New, Comment
# Register your models here.

admin.site.register(Category)

class AdminNew(admin.ModelAdmin):
    list_display = ('title', 'category', 'add_time')

admin.site.register(New, AdminNew)

class AdminComment(admin.ModelAdmin):
    list_display = ('new', 'name','email', 'comment', 'status')

admin.site.register(Comment, AdminComment)