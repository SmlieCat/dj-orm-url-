from django.db.models import Count
from django.shortcuts import render, redirect, reverse
from .models import Article, ArticleCategory, ArticleTag, OtherUser
from .forms import LoginForm, RegistForm, InfoForm, PasswordForm, UserDelForm
from django.contrib import messages



def index(request):


    return render(request, 'index.html')


#文章首页
def article_list(request):

    article_list = Article.objects.all().order_by('-created_time')
    date_list = Article.objects.dates('created_time', 'month', order='DESC')
    categorys = ArticleCategory.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
    tags = ArticleTag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)

    return render(request, 'article_list.html', locals())


#文章详情
def article_detail(request, id):

    article = Article.objects.get(id=int(id))
    article_list = Article.objects.all().order_by('-created_time')[:5]
    date_list = Article.objects.dates('created_time', 'month', order='DESC')
    categorys = ArticleCategory.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
    tags = ArticleTag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)

    article.click_num += 1
    article.save()

    return render(request, 'article_detail.html', locals())



#归档跳转
def article_archives(request, year, month):

    article_list = Article.objects.filter(created_time__year=year, created_time__month=month).order_by('-created_time')
    date_list = Article.objects.dates('created_time', 'month', order='DESC')
    categorys = ArticleCategory.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
    tags = ArticleTag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
    return render(request, 'article_list.html', locals())



#分类跳转
def article_category(request, id):

    article_list = Article.objects.filter(category=int(id)).order_by('-created_time')
    date_list = Article.objects.dates('created_time', 'month', order='DESC')
    categorys = ArticleCategory.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
    tags = ArticleTag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
    return render(request, 'article_list.html', locals())


#标签跳转
def article_tag(request, id):

    article_list = Article.objects.filter(tags=int(id)).order_by('-created_time')
    date_list = Article.objects.dates('created_time', 'month', order='DESC')
    categorys = ArticleCategory.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
    tags = ArticleTag.objects.annotate(num_posts=Count('article')).filter(num_posts__gt=0)
    return render(request, 'article_list.html', locals())


#注册
def user_regist(request):
    form = RegistForm()
    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        user_password2 = request.POST['user_password2']
        user_email = request.POST['user_email']
        user_phone = request.POST['user_phone']
        user_desc = request.POST['user_desc']

        if OtherUser.objects.filter(name=user_name):
            messages.error(request, '用户已存在，请重新输入！')
            return redirect(reverse('user_regist'))
        else:
            if user_password == user_password2:
                otheruser = OtherUser(name=user_name, password=user_password, email=user_email,
                                      phone=user_phone, desc=user_desc)
                otheruser.save()
                messages.success(request, '注册成功，请登录！')
                return redirect(reverse('user_login'))
            else:
                messages.error(request, '密码输入不一致，请重新输入！')
    return render(request, 'user_regist.html', locals())



#登录
def user_login(request):
    form = LoginForm()

    if request.method == 'POST':
        user_name = request.POST['user_name']
        user_password = request.POST['user_password']
        user = OtherUser.objects.filter(name=user_name)
        if user:
            if str(user_password) == str(user[0].password):

                messages.success(request, '登录成功！')
                request.session['user_name'] = user_name
                request.session['user_id'] = user[0].id

                return redirect(reverse('index'))
            else:
                messages.error(request, '用户密码不正确，请重新输入！')
                return redirect(reverse('user_login'))
        else:
            messages.error(request, '用户不存在，请重新输入！')

    return render(request, 'user_login.html', locals())



#退出
def user_logout(request):
    del request.session['user_name']
    messages.success(request, '退出成功！')
    return redirect(reverse('index'))



#个人中心
def user_center(request):

    return render(request, 'user_center.html')


#个人详情
def user_detail(request):
    user = OtherUser.objects.filter(name=request.session.get('user_name'))[0]

    return render(request, 'user_detail.html', locals())



#修改资料
def user_info(request):

    user = OtherUser.objects.filter(name=request.session.get('user_name'))[0]
    #表单回填
    form = InfoForm(initial={'user_name': user.name, 'user_email': user.email, 'user_phone': user.phone,
                             'user_desc': user.desc})
    if request.method == 'POST':
        user.name = request.POST['user_name']
        user.email = request.POST['user_email']
        user.phone = request.POST['user_phone']
        user.desc = request.POST['user_desc']
        user.save()
        messages.success(request, '修改成功！')
        return redirect(reverse('user_detail'))

    return render(request, 'user_info.html', locals())



#修改密码
def user_password(request):
    form = PasswordForm()
    if request.method == 'POST':
        old_password = request.POST['old_password']
        user_password = request.POST['user_password']
        user_password2 = request.POST['user_password2']
        user = OtherUser.objects.filter(name=request.session.get('user_name'))[0]
        if old_password == user.password:
            if user_password == user_password2:
                user.password = user_password
                user.save()
                del request.session['user_name']
                messages.success(request, '修改密码成功, 请重新登录')
                return redirect(reverse('user_login'))
            else:
                messages.error(request, '密码不一致，请重新输入！')
                return redirect(reverse('user_password'))
        else:
            messages.error(request, '原密码错误，请重新输入！')
    return render(request, 'user_password.html', locals())




#注销个人账户
def user_del(request):
    form = UserDelForm()
    if request.method == 'POST':
        user = OtherUser.objects.filter(name=request.session.get('user_name'))[0]
        user_password = request.POST['user_password']
        if user.password == user_password:
            pass
        else:
            messages.error(request, '密码错误，请重新输入！')
    return render(request, 'user_del.html', locals())



#相册列表
def album_list(request):

    return render(request, 'album_list.html')



#相册详情
def album_browse(request):

    return render(request, 'album_browse.html')