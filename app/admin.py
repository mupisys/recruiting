from django.contrib import admin
from .models import Category, Post, Message, Comment

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Message)
admin.site.register(Comment)
