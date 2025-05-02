from django.contrib import admin

from .models import Comment, Follow, Group, Post


class PostAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'pub_date',
        'author',
        'group'
    )
    list_editable = (
        'group',
    )
    search_fields = ('text',)
    list_display_links = ('text',)


class PostInline(admin.StackedInline):
    model = Post
    extra = 0


class GroupAdmin(admin.ModelAdmin):
    inlines = (
        PostInline,
    )
    list_display = (
        'title',
        'description',
        'slug',
    )
    search_fields = ('title',)


class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'text',
        'author',
        'post',
        'created',
    )
    search_fields = ('author',)


class FollowAdmin(admin.ModelAdmin):
    list_display = (
        'following',
        'user',
    )
    search_fields = ('following',)


admin.site.register(Group, GroupAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(Follow, FollowAdmin)
admin.site.empty_value_display = 'Не задано'
