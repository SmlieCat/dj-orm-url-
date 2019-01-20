from django.forms import Form
from django.forms import widgets
from django.forms import fields




#用户注册
class RegistForm(Form):

    user_name = fields.CharField(min_length=3, max_length=10,

                             widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '输入用户名'}))


    user_password = fields.CharField(min_length=3, max_length=15,

                             widget=widgets.PasswordInput(attrs={'class': "form-control", 'placeholder': '输入密码'}))


    user_password2 = fields.CharField(min_length=3, max_length=15,

                                     widget=widgets.PasswordInput(
                                         attrs={'class': "form-control", 'placeholder': '确认密码'}))


    user_phone = fields.CharField(required=False, min_length=0, max_length=20,

                             widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '联系方式'}))


    user_email = fields.CharField(required=False, min_length=0, max_length=20,

                             widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '邮箱'}))


    user_desc = fields.CharField(required=False, min_length=0, max_length=100,
                            widget=widgets.Textarea(attrs={'class': "form-control", 'placeholder': '签名',
                                                           'cols': '1', 'rows': '2'}))



#用户登录
class LoginForm(Form):

    user_name = fields.CharField(min_length=3, max_length=10,

                             widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '输入用户名'}))


    user_password = fields.CharField(min_length=3, max_length=15,

                             widget=widgets.PasswordInput(attrs={'class': "form-control", 'placeholder': '输入密码'}))




#修改个人资料
class InfoForm(Form):

    user_name = fields.CharField(min_length=3, max_length=10,

                             widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '输入用户名'}))


    user_phone = fields.CharField(required=False, min_length=0, max_length=20,

                             widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '联系方式'}))


    user_email = fields.CharField(required=False, min_length=0, max_length=20,

                             widget=widgets.TextInput(attrs={'class': "form-control", 'placeholder': '邮箱'}))


    user_desc = fields.CharField(required=False, min_length=0, max_length=100,
                            widget=widgets.Textarea(attrs={'class': "form-control", 'placeholder': '签名',
                                                           'cols': '1', 'rows': '2'}))



#修改个人密码
class PasswordForm(Form):

    old_password = fields.CharField(min_length=3, max_length=15,

                                     widget=widgets.PasswordInput(
                                         attrs={'class': "form-control", 'placeholder': '输入密码'}))

    user_password = fields.CharField(min_length=3, max_length=15,

                                     widget=widgets.PasswordInput(
                                         attrs={'class': "form-control", 'placeholder': '输入密码'}))

    user_password2 = fields.CharField(min_length=3, max_length=15,

                                      widget=widgets.PasswordInput(
                                          attrs={'class': "form-control", 'placeholder': '确认密码'}))

#注销
class UserDelForm(Form):

    user_password = fields.CharField(min_length=3, max_length=15,

                                     widget=widgets.PasswordInput(
                                         attrs={'class': "form-control", 'placeholder': '输入密码'}))