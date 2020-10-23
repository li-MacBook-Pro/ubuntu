
from django.shortcuts import render, redirect, reverse

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Permission, Group

# Create your views here.


def home(request):
    username = request.session.get('username', '未登录')
    return render(request, 'templates/user/log/home.html', context={
        'username': username
    })


def login(request):
    if request.method == 'GET':
        return render(request, 'templates/user/log/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        # request.session['username'] = username
        # request.session.set_expiry(value=None)  # 不过期
        login(request, username)
        return redirect(reverse('home'))
