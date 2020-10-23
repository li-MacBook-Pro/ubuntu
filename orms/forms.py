
from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=25, min_length=2)
    password = forms.CharField(max_length=25, min_length=2)


class AddForm(forms.Form):
    first = forms.CharField(max_length=25, min_length=2)
    second = forms.CharField(max_length=25, min_length=2)


class RegisterFrom(forms.Form):
    # username = forms.CharField(min_length=6)
    username = forms.CharField(min_length=2)
    password = forms.CharField(min_length=6,
                               widget=forms.PasswordInput(
                                   attrs={'placeholder': '请输入密码'}),
                               error_messages={'min_length': '密码长度小于6',
                                               'max_length': '密码长度超过8了'})

    password_repeat = forms.CharField(widget=forms.PasswordInput())
    email = forms.EmailField()

