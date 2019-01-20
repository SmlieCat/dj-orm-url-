from django.contrib import admin
from .models import Article, ArticleTag, ArticleCategory, OtherUser, SeePower, Album,\
    AlbumTag, AlbumCategory, AlbumFavor, Photo


class ArticleAdmin(admin.ModelAdmin):

    list_display = ['title', 'created_time', 'category', 'author']

class OtherUserAdmin(admin.ModelAdmin):

    list_display = ['name', 'password', 'email', 'phone', 'addtime']



admin.site.register(ArticleCategory)
admin.site.register(ArticleTag)
admin.site.register(Article, ArticleAdmin)
admin.site.register(OtherUser, OtherUserAdmin)


admin.site.register(Album)
admin.site.register(Photo)
admin.site.register(AlbumFavor)
