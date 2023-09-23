from django.contrib import admin

from .models import Post, PostFile , Comment , Like


class PostFileInLineAdmin(admin.StackedInline):
    model = PostFile
    fields = ('files' , )
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'is_active', 'created_time')
    inlines = (PostFileInLineAdmin, )


@admin.register(PostFile)
class PostFileAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_approved')
    list_filter = ('is_approved',)
    date_hierarchy = 'created_time'


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('post', 'user', 'is_liked')
    list_filter = ('is_liked',)
    date_hierarchy = 'created_time'