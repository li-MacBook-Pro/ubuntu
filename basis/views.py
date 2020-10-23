import datetime
import pprint

from django.shortcuts import render, redirect, reverse

from django.http.response import JsonResponse, HttpResponse

from . import models
# from django_redis import get_redis_connection


# rds=get_redis_connection('default')


# Create your views here. request

def one(request, xx):
    if xx == 'new':
        return redirect(reverse('new_version'))
    print('{}:'.format(xx), type(xx))
    # return HttpResponse('hello {}'.format(xx))
    return render(request, 'html/label/stencil_label.html', context={
        'name_xx': xx
    })


def two(request):

    return HttpResponse('hello {}'.format('re_path设置'))


def three(request):

    return HttpResponse('New Version: I Like Computer and artificial intelligence {}'.format('0'))


def four(request):
    name = '憨憨'
    return render(request, 'html/index.html', context={
        'name': name
    })


class Fruits:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def say(self):
        return 'HA'


ap = Fruits('apple','red')
ls = ['x', 'y', 'z']
dc = {'a': 1, 'b': 2}


def six():
    return 'django'


def seven(request):
    test = 'THIS IS A LIST!'
    return render(request, 'html/label/stencil_label.html', context={
        'username': 'test',  # 字符串
        'foo': [i for i in range(10)],
        'hello': six,  # 函数
        'fruits_say': ap.say,  # 方法
        'fruits': ap,  # 类对象
        'list': ls,  # 列表
        'dict': dc,  # 字典
        'test': test,
        'xx': '',
        'num1': 1,
        'num2': 2,
        'now': datetime.datetime.now,
        'html': '<h1>hello django</h1>',
        'float': 3.1415926,
    })


def eight(request):

    return render(request, 'html/inherit/Quote.html')


def custom(request):
    ts = 'HELLO   hello'
    format_str = '%Y-%m-%d %H:%M:%S'
    person = {
            'name': request.GET.get('username'),
            'age': request.GET.get('age'),
        }
    person1 = {
            'name': request.GET.get('username'),
            'age': request.GET.get('age'),
        }
    return render(request, 'html/custom/filter_zero.html', context={
        'ts': ts,
        'format_str': format_str,
        'username': 'li',
        'password': 'li123',
        'person': person,
        'person1': person1,
        'news': [
        ],

    })


def nine(request,username):
    name=request.GET['username']
    # password=request.GET['password']
    return render(request, 'html/custom/filter_zero.html', context={
        'username': name,
    })


def ten(request):
    # pprint.pprint(requset.META)
    # print(requset.user)
    print(request.method)  # GET方法
    return render(request, 'html/custom/filter_zero.html')


def eleven(request):
    dc={
        'name': '李',
        'name1': 'li',
        'age': '18',
    }
    return JsonResponse(data=dc,json_dumps_params={
        # 'ensure_ascii': True,
        'ensure_ascii': False,
    })


def twelve(request, name):
    return render(request, 'html/custom/filter_zero.html', context={
        'version': name,
    })


def thirteen(request):
    return render(request, 'html/custom/filter_zero.html', context={
        'for_list': [n for n in range(10)],
        'for_None': [],
        'format_string': '%Y-%m-%d %H:%M:%S',
        'username': 'li',
        'password': 'li123',
        'person': {
            'name': request.GET.get('username'),
            'age': request.GET.get('age'),
        },
        'person1': {
            'name': request.GET.get('username'),
            'age': request.GET.get('age'),
        },
        'news': [

        ],
    })


def fourteen(request, version):
    return render(request, 'html/custom/filter_zero.html', context={
        'version': version,
    })



# from django.shortcuts import render, redirect, reverse
# from django.http.response import JsonResponse, HttpResponse
#
# from .models import Users
# from django_redis import get_redis_connection


# def orm_one(request):
#     users = Users.objects.all()
#     return render(request, 'html/mysql_orm/one.html', context={
#         'users': users
#     })
#
#
# def add_users(request):
#     users = Users(name='edge teacher', age=29, gender='True')
#     users.save()
#     return HttpResponse('Added successfully！')
#
#
# def delete_users(request):
#     users = Users.objects.get(id=2)
#     users.delete()
#     return HttpResponse('successfully deleted！')
#
#
# def update_users(request):
#     # users = Users.objects.get(id=3)
#     # users.name = 'coco Teacher'
#     # users.save()
#     # Users.objects.filter(name='画龙Teacher').update(name='edge_Teacher')
#     Users.objects.update(age=30)
#     return HttpResponse('Successfully modified！')
#
#
# def select_users(request):
#     select = Users.objects.all()
#     return HttpResponse('search successful！')
#
#
