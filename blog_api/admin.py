from django.contrib import admin
from .models import Post, Tag, User

admin.site.register(Tag);
admin.site.register(Post);