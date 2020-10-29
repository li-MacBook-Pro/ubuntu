import os

import requests
from lxml import etree

from django.shortcuts import render, redirect, reverse
from django.http.response import JsonResponse, HttpResponse

from .models import Student, Department, UserModel, ip

from django.db.models import Max, Min, Sum, Count, Avg
from django.db.models import Q, F

from django.views import View

from django21.settings import MEDIA_ROOT

from .forms import AddForm, RegisterFrom, LoginForm

from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.models import User, Permission, Group

# from django_redis import get_redis_connection


# rds=get_redis_connection('default')


# Create your views here. request


# def orm_one(request):

#     users = Users.objects.all()
#     return render(request, 'html/mysql_orm/one.html', context={
#         'users': users
#     })


def add_s(request):

    # users
    # users = Users(name='edge teacher', age=29, gender='True').save()

    # student
    # s = Student(s_id=1, s_name='张三', departments_id=1).save()

    # Department
    # d = Department(d_id=5, d_name='C++').save()
    d = Department.objects.create(d_id=6, d_name='AI')

    return HttpResponse('Added successfully！')


# def delete(request):
#
#     # users
#     users = Users.objects.get(id=2)
#     users.delete()
#
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


def select_s(request):

    # Student
    # s = Student.objects.filter(departments__d_name='C')

    c = Department.objects.get(d_id=1)
    s = Student.objects.all().filter(departments=c)

    # # 聚合查询
    # r = Student.objects.aggregate(Avg('age'))
    # a = Student.objects.aggregate(average_age=Avg('age'))  # 指定一个name
    # b = Student.objects.aggregate(Avg('age'), Max('age'), Min('age'), Sum('age'))
    #
    # # 分组查询
    # # 一对多
    # d = Student.objects.values('departments')  # 拿到学生表分组的字段
    # e = Student.objects.values().annotate(count=Count('departments')).values('departments_id', 'count')
    # g = Student.objects.values().annotate(count=Count('departments'))  # 对departments字段进行分组
    # # 分组后按照需要字段输出
    # h = Student.objects.values().annotate(count=Count('departments')).values('departments__d_name', 'count')
    # # 多对多
    # i = Student.objects.all()  # 以课程作为分组条件查每个课程学生的数量  拿到所有课程的数据
    #
    # # F查询  针对两个字段的值进行比较
    # f = Student.objects.filter(departments_id__gt=F('s_id'))  # 学院ID小于学生学号的
    # j = Student.objects.all().update(age=F('age')+1)  # 所有人年龄加1岁
    #
    # # Q查询 &（and）、｜（or）、~（not）取反
    # k = Student.objects.filter(Q(s_name='name_1') | Q(s_name='name_2'))
    # m = Student.objects.filter(Q(s_name='name_3') & ~ Q(age=23))

    print(s)

    return HttpResponse('search successful！')


def static_test(request):
    return render(request, 'templates/base/base.html')


def request_test(request):
    print(request.path, request.method)
    return render(request, 'html/Get_Post/GP.html')


def get_test(request):

    a = request.GET.get('name_a')
    b = request.GET.get('b')
    c = request.GET.get('c')

    print(request.path, request.method)
    print(a, b, c)

    return HttpResponse('Get success')
    # return render(request, 'html/Get_Post/GP.html')


def post_test(request):

    print(request.path, request.method)

    if request.method == 'GET':

        a = request.GET.get('name_a')
        b = request.GET.get('b')
        print(a, b)

        return render(request, 'html/Get_Post/GP.html')

    elif request.method == 'POST':

        a = request.POST.get('name_a')
        b = request.POST.get('name_b')
        print(a, b)

        return render(request, 'html/Get_Post/GP.html')

    else:
        return HttpResponse('这个不是请求')


# from django.db import transaction
#
#
# def post_get(request):
#     try:
#         with transaction.atomic():
#             title = request.POST.get('title'),
#             author = request.POST.get('author'),
#             cid = request.POST.get('cid'),
#             desc = request.POST.get('desc'),
#             img_url = '/static/image/1.JPG'
#             print()
#
#             # cata
#             cty = NewCategory.objects.get(id=int(cid[0]))  # 分类
#             at = Author.objects.get(id=int(author[0]))  # 作者
#
#             News.objects.create(
#                 title=title,
#                 img_url=img_url,
#                 desc=desc,
#                 category=cty,
#                 author=at,
#             )
#
#     except Exception as e:
#         transaction.rollback()  # 进行回滚操作
#         print(e)
#     return HttpResponse(content="success", status=200)


# 类视图


class UserApiView(View):  # View-->

    # http_method_names = ['get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace']
    http_method_names = View.http_method_names + []  # 新增方法

    def get(self, request):
        return HttpResponse('get 方法执行')

    def post(self, request):
        # print(request.POST.get('title'), request.POST.get('content'))
        return HttpResponse('post 方法执行')

    def put(self, request):
        return HttpResponse('put 方法执行')

    def patch(self, request):
        return HttpResponse('get 方法执行')

    def delete(self, request):
        return HttpResponse('delete 方法执行')

    def head(self, request):
        return HttpResponse('head 方法执行')

    # def options(self, request):# 不清楚
    #     return HttpResponse('options 方法执行')

    def trace(self, request):
        return HttpResponse('get 方法执行')

    def uploads(self, request):

        pass


def uploads_test(request):
    if request.method == 'GET':

        # return HttpResponse('get 方法执行')
        return render(request, 'html/upload/upload.html')
    elif request.method == 'POST':

        # f_get = request.FILES('file')
        f_get = request.FILES.get('file')
        # f_get = request.FILES.getlist('file')

        f_name = os.path.join(MEDIA_ROOT, f_get.name)

        # # 读取文件 类似于生成器
        with open(f_name, 'wb') as f:
            # chunks() get data 字节类型的数据
            def test():
                def foo():
                    for n in range(100):
                        yield n
                for i in foo():
                    if i < 50:
                        print(i)

            for fb in f_get.chunks():
                f.write(fb)

            return HttpResponse('上传成功')

    else:
        return HttpResponse('不是请求')


def set_ck(request):
    response = HttpResponse('设置cookie')
    response.set_cookie('name', 'set_cookie')
    return response


def get_ck(request):
    cookie = request.COOKIES
    print(cookie)
    return HttpResponse('获取cookie')


def delete_ck(request):
    rs = HttpResponse('删除cookie')
    rs.delete_cookie('name')
    return rs


def home(request):
    username = request.session.get('username', '未登录')
    return render(request, 'templates/user/log/home.html', context={
        'username': username
    })


def login1(request):
    if request.method == 'GET':
        return render(request, 'templates/user/log/login.html')
    elif request.method == 'POST':
        username = request.POST.get('username')
        request.session['username'] = username
        request.session.set_expiry(0)  # 关闭浏览器就过期
        # request.session.set_expiry(value=None)  # 不过期
        # login(request, username)
        # login(request, username)  # TypeError: login() takes 1 positional argument but 2 were given
        # login(request, user=username)  # TypeError: login() got an unexpected keyword argument 'user'
        return redirect(reverse('home'))


def logout1(request):
    request.session.flush()
    # logout(request)
    return redirect(reverse('home'))


def add_form(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            a = form.changed_data['a']
            b = form.changed_data['b']
            # return HttpResponse(str(int(a)) + str(int(b)))
            return HttpResponse(str(int(a) + int(b)))
    # else:
    #     form = AddForm()
    # return render(request, '', {'form',form})
        else:
            form = AddForm()
    return render(request, 'html/form/add_form.html')


def register(request):
    if request.method == 'GET':
        form = RegisterFrom()
        return render(request, 'html/form/add_form.html',
                      context={'form': form})
    elif request.method == 'POST':
        form = RegisterFrom(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            password_repeat = form.cleaned_data.get('password_repeat')
            email = form.cleaned_data.get('email')
            if password == password_repeat:
                user = UserModel.objects.create(username=username,
                                                password=password,
                                                email=email)
                return HttpResponse('注册成功!')
            else:
                return HttpResponse('注册失败!')
        else:
            return HttpResponse('注册失败!')


class LoginView(View):
    def get(self, request):
        return render(request, 'html/form/add_form.html', context={
            'form': LoginForm
        })

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        us = UserModel.objects.filter(username=username)

        # form表单操作~~~~~~
        form = LoginForm(data=request.POST)
        if not form.is_valid():
            return HttpResponse('账户或密码错误')
        us = UserModel.objects.filter(username=form.cleaned_data['username'])

        if not us.exists():
            return HttpResponse('用户不存在')
        if us.first().password != password:
            return HttpResponse("密码错误")

        # cookies
        response = HttpResponse('登录成功')
        response.set_cookie('uid', us.first().id)  #
        print(us.first().id)
        response.set_cookie('name', us.first().username)  #
        print(response.set_cookie('name', us.first().username))
        # session
        # 不能直接使用us.first().id、需要加一个前缀'test' + str(us.first().id)
        request.session['test' + str(us.first().id)] = us.first().username

        return response


class T_demo(View):

    def get(self, request):

        ip_1 = request.META['REMOTE_ADDR']

        data = {
            'ip': ip_1,
        }

        url = 'http://ip.tool.chinaz.com/'  # 27.206.33.238

        user_agent = request.META['REMOTE_ADDR']

        headers = {
            'user-agent': user_agent,
        }

        res = requests.post(url, data=data, headers=headers)

        html = etree.HTML(res.text)

        my_ip_1 = html.xpath('//div[contains(@class,"WhoIpWrap")]/p[1]/span[1]/text()')  # 27.206.33.238
        my_ip_2 = html.xpath('//div[contains(@class,"WhoIpWrap")]/p[2]/span[1]/text()')  # 27.206.33.238

        my_ip_number_1 = html.xpath('//div[contains(@class,"WhoIpWrap")]/p[1]/span[3]/text()')  # 466493934
        my_ip_number_2 = html.xpath('//div[contains(@class,"WhoIpWrap")]/p[2]/span[3]/text()')  # 466493934

        address_1 = html.xpath('//div[contains(@class,"WhoIpWrap")]/p[1]/span[4]/text()')  # 山东省菏泽市 联通
        address_2 = html.xpath('//div[contains(@class,"WhoIpWrap")]/p[2]/span[4]/text()')  # 山东省菏泽市 联通

        ll_1 = html.xpath('//div[contains(@class,"locationContent")]//div[8]/div[1]/text()')
        ll_2 = html.xpath('//div[contains(@class,"locationContent")]//div[8]/div[2]/text()')  # 经纬度

        radius_1 = html.xpath('//div[contains(@class,"locationContent")]//div[10]/div[1]/text()')  # 覆盖半径
        radius_2 = html.xpath('//div[contains(@class,"locationContent")]//div[10]/div[2]/text()')

        postal_1 = html.xpath('//div[contains(@class,"locationContent")]//div[11]/div[1]/text()')  # 邮政编码：
        postal_2 = html.xpath('//div[contains(@class,"locationContent")]//div[11]/div[2]/text()')

        # print('{}:{}  {}:{}  {}:{}  {}:{}  {}:{}  {}:{}'
        #       .format(my_ip_1, my_ip_2, my_ip_number_1, my_ip_number_2, address_1, address_2,
        #               ll_1, ll_2, radius_1, radius_2, postal_1, postal_2))
        db_ip = ip.objects.all().values('ip')

        db_l_l = '无数据'
        db_ip_orms = {'ip': str(my_ip_2[0])}

        def add_to():
            ip.objects.create(
                ip=str(my_ip_2[0]),
                number=str(my_ip_number_2[0]),
                address=str(address_2[0]),
                l_l=str(ll_2[0]),
                radius=str(radius_2[0]),
                postal=str(postal_2[0]),
            ).save()

        for i in db_ip:
            if str(my_ip_2[0]) == i['ip']:
                a = ip.objects.filter(ip=str(i['ip'])).values()
                if a[0]['l_l'] == db_l_l:
                    a.update(l_l=str(ll_2[0]))
                if a[0]['number'] != str(my_ip_number_2[0]):
                    a.update(number=str(my_ip_number_2[0]))
                if a[0]['address'] != str(address_2[0]):
                    a.update(address=str(address_2[0]))
                if a[0]['radius'] != str(radius_2[0]):
                    a.update(radius=str(radius_2[0]))
                if a[0]['postal'] != str(postal_2[0]):
                    a.update(postal=str(postal_2[0]))

        if db_ip_orms not in db_ip:
            add_to()

        context = {
            'qwe123': '：',

            'ip_1': my_ip_1[0],
            'ip': my_ip_2[0],

            'my_ip_number_1': my_ip_number_1[0],
            'my_ip_number': my_ip_number_2[0],

            'address_1': address_1[0],
            'address': str(address_2[0]).split(' ')[0],

            'll_1': ll_1[0],
            'll_2': ll_2[0],

            'radius_1': radius_1[0],
            'radius_2': radius_2[0],

            'postal_1': postal_1[0],
            'postal_2': postal_2[0],

        }

        return render(request, 'html/xpath/xpath.html', context)


class numpy_(View):
    def get(self, request):
        return render(request, 'html/numpy_/numpy_.html')
