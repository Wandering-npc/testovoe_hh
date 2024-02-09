from django.contrib import admin

from api.models import Post, User

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
