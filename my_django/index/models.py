from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from datetime import datetime
from uuid import uuid4



#文章分类表
class ArticleCategory(models.Model):

    name = models.CharField('分类', max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '文章分类'
        verbose_name_plural = '文章分类'

#文章标签表
class ArticleTag(models.Model):

    name = models.CharField('标签', max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '文章标签'
        verbose_name_plural = '文章标签'

#文章表
class Article(models.Model):

    title = models.CharField('标题', max_length=70)
    body = RichTextField('正文')
    created_time = models.DateTimeField('发布日期')
    excerpt = models.CharField('摘要', max_length=200, blank=True)
    click_num = models.IntegerField('阅读量', default=0)
    category = models.ForeignKey(ArticleCategory, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(ArticleTag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '文章正文'
        verbose_name_plural = '文章正文'



#用户表
class OtherUser(models.Model):
    name = models.CharField('名字', max_length=20)
    password = models.CharField('密码', max_length=20)
    email = models.CharField('邮箱', max_length=20)
    phone = models.CharField('联系方式', max_length=50)
    desc = models.CharField('个人签名', max_length=200)
    uuid = models.CharField('用户标识', max_length=100, default=uuid4().hex)
    addtime = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '普通用户'
        verbose_name_plural = '普通用户'



#权限表
class SeePower(models.Model):

    name = models.CharField('权限', max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '权限'
        verbose_name_plural = '权限'


#相册分类表
class AlbumCategory(models.Model):

    name = models.CharField('相册分类', max_length=100)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = '相册分类'
        verbose_name_plural = '相册分类'


#相册标签表
class AlbumTag(models.Model):

    name = models.CharField('相册标签', max_length=100)
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '相册标签'
        verbose_name_plural = '相册标签'



#相册表
class Album(models.Model):

    title = models.CharField('标题', max_length=70)
    desc = models.CharField('介绍', max_length=200)
    click_num = models.IntegerField('阅读量', default=0)
    favor_num = models.IntegerField('收藏量', default=0)
    category = models.ForeignKey(AlbumCategory, on_delete=models.CASCADE, verbose_name='分类')
    tags = models.ManyToManyField(AlbumTag, blank=True, verbose_name='标签')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='作者')
    power = models.ForeignKey(SeePower, on_delete=models.CASCADE, verbose_name='权限')
    addtime = models.DateTimeField('创建时间', default=datetime.now)
    def __str__(self):
        return self.title
    class Meta:
        verbose_name = '相册'
        verbose_name_plural = '相册'




#图片表
class Photo(models.Model):

    photo_url = models.CharField('图片链接', max_length=200, blank=True)
    album = models.ForeignKey(Album, on_delete=models.CASCADE, verbose_name='相册')
    addtime = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.photo_url
    class Meta:
        verbose_name = '图片链接'
        verbose_name_plural = '图片链接'



#收藏的相册
class AlbumFavor(models.Model):

    user = models.ManyToManyField(OtherUser, blank=True, verbose_name='用户')
    album = models.ManyToManyField(Album, blank=True, verbose_name='相册')
    addtime = models.DateTimeField('创建时间', default=datetime.now)

    def __str__(self):
        return self.user
    class Meta:
        verbose_name = '用户'
        verbose_name_plural = '用户'