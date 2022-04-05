# Register your models here.

from django.contrib import admin
from .models import Post, Comment


class CommentAdminInLine(admin.TabularInline):
    model = Comment
    fields = ['text']
    extra = 0
    
class PostAdmin(admin.ModelAdmin):
    list_display = [
            'id','title','text',
            'is_enable','publish_data',
            'created_time','updated_time'
            ]

    inlines = [CommentAdminInLine]

class CommentAdmin(admin.ModelAdmin):
    list_display =[
            'post','text',
            'created_time','updated_time'
            ]    

admin.site.register(Post,PostAdmin)

# admin.site.register(Comment,CommentAdmin)

