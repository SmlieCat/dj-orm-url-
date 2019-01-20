from django.urls import path
from . import views



urlpatterns = [
    path('', views.index, name='index'),
    path('article/list/', views.article_list, name='article_list'),
    path('article/detail/<int:id>', views.article_detail, name='article_detail'),
    path('article/archives/<int:year>/<int:month>', views.article_archives, name='article_archives'),
    path('article/category/<int:id>', views.article_category, name='article_category'),
    path('article/tag/<int:id>', views.article_tag, name='article_tag'),
    path('user/regist/', views.user_regist, name='user_regist'),
    path('user/login/', views.user_login, name='user_login'),
    path('user/logout/', views.user_logout, name='user_logout'),
    path('user/center/', views.user_center, name='user_center'),
    path('user/detail/', views.user_detail, name='user_detail'),
    path('user/info/', views.user_info, name='user_info'),
    path('user/password/', views.user_password, name='user_password'),
    path('user/del/', views.user_del, name='user_del'),
    path('album/list/', views.album_list, name='album_list'),
    path('album/browse/', views.album_browse, name='album_browse'),
]

