from django.contrib import admin

from .models import  Book, Comment

@admin.register(Comment)  #admin.site.register(Comment, CommentAdmin)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'book', 'text', 'datetime_create', 'is_active', 'recommend')


admin.site.register(Book)
