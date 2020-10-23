# import os, random
# import sys
#
# import django
#
# # 准备django 目录 并插入解释寻包路径
# project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程目录
# # print(project)
# sys.path.insert(0, project)
#
# # 载入django 环境
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django01.settings')
#
# django.setup()
#
# # 导入自定义的模型类
#
# from demo0.models import Users, Student, Classes, StuCard, Teacher, Order, Spu
#
# # django事务
# from django.db import transaction
#
# # django事务：数据库操作要放在事务里面，把数据操作看成一种操作，成功或者失败，有错误就不执行数据库操作
#
# def transaction_use():
#     try:
#         with transaction.atomic():
#             cls1 = Classes.ordering.create(name='demo')
#             # 薅羊毛案例
#             # 创建一个数据（订单表）（商品数量）等。。。里面打折的商品只有十个、原价一万，打折完两千
#             # 1：下单5个
#             # 2：下单5个
#             # 3：下单五个
#
#             # raise Exception()  # 出错抛出问题
#
#             Teacher.objects.create(
#                 name='demo'
#             ).classes.add()
#             #  仓库打折的数量为10
#             #  1：减去5个
#             #  2：出错误了，打折的商品没有减去五个，损失一万，
#             #  3：出错误了，打折的商品没有减去五个，损失一万
#     except Exception as e:
#         transaction.rollback()  # 进行回滚操作
#         print(e)
#
# class CDUS():
#     # create增
#     def create(self, vname, vgender, age):
#         user = Users.objects.create(
#             name=vname,
#             gender=vgender,
#             age0=age,
#         )
#         # user.save()
#         # print(user)
#         # print(user.name)
#
#     def create_1(self, n):
#         import random
#         x = ['male', 'Female']
#         for i in range(n):
#             CDUS().create('demo%s' % i, random.choice(x), random.randint(18, 28))
#     # select查
#     def select_1(self, vname):
#         try:
#             user = Users.objects.get(
#                 id=vname,
#                 # name=vname
#             )  # get例如：名字相同的有两个，这样获取就会报错；查询不存在的数据也会报错。
#             # print('id={}：name={}'.format(vname, user.name))
#             print(user.gender)
#             return user
#         except Users.DoesNotExist as e:
#             print(e)
#
#     def select_2(self):
#         users = Users.objects.all()  # 并没有执行sql语句
#         print(users)
#
#     def select_3(self):
#         users = Users.objects.filter(
#             gender='m'
#         )  # 执行sql  --- where
#         # print(users)
#         # print(users.values())
#         # print(list(users.values()))
#         # QuerySet = users.values()
#         # print(QuerySet)
#         # for i in range(len(QuerySet)):
#         #     print('下标{} {} {}'.format(i, QuerySet[0].keys(), QuerySet[0].values()))
#         # for key in QuerySet[0].keys():
#         #     for i in range(len(QuerySet)):
#         #         print('这是下标为：{}，key为：{}的数据'.format(i, QuerySet[i][key]))
#         print(users.values_list())
#         # 形成类似json 格式的数据
#         for user in users.values():
#             print(user)
#
#     # update
#     def update(self):
#         user = CDUS().select_1(1)  # 找到数据
#         user.name = 'demo2'  # 修改数据
#         user.save()  # save() 会把每个字段都更新一遍
#         print('修改之后：name={}'.format(user.name))
#
#     # delete
#     def delete_1(self, data):
#         user = Classes.objects.get(id=data)
#         # user = Users.objects.get(name=data)
#         user.delete()
#
# # create增
# class C():
#
#     # create增
#     def create_0(self, name, gender, birthday, age, phone):
#         std = Student.objects.create(
#             name=name,
#             gender=gender,
#             age=age,
#             birthday=birthday,
#             phone=phone,
#         )
#         std.save()
#
#     def create(self, n):
#         import random
#         x = ['male', 'Female']
#         for i in range(n):
#             C().create_0('name--%s' % i, random.choice(x), None, random.randint(18, 28), random.randint(11111, 20000))
#
# # select查
# class S():
#     def exclude_0(self):
#         stds = Student.objects.exclude(
#             name='demo0'
#         )
#         print(stds.values())
#
#     def select_(self):
#         # std_first = Student.objects.first()
#         # std_first = Student.objects.all()[0:5].values()[0]['name']
#         # std_first = Student.objects.first()
#         # print(Student.objects.first().name)
#         # std_last = Student.objects.last()
#         # print(Student.objects.last().name)
#
#         #where 条件查询，条件是and关系
#         # std_filter = Student.objects.filter(id=1)
#         # std_filter = Student.objects.filter(id=1)
#         # print(Student.objects.filter(id__exact=1).values()[0]['id'])
#         # print(Student.objects.filter(id__iexact=1).values()[0]['id'])
#         # print(Student.objects.filter(id=1, ).values())
#         # print(Student.objects.filter(id=1, name='').values())  # and关系
#         # print(Student.objects.filter(id=1, ).values().first()['id'])
#         # print(Student.objects.filter(id__gt=1).values().first()['id'])
#         # print(Student.objects.filter(id__gt=1).first().id)
#         # print(Student.objects.filter(id__gte=1).values().first()['id'])
#         # print(Student.objects.filter(id__lt=2).values().first()['id'])
#         # print(Student.objects.filter(id__lte=1).values().first()['id'])
#         # print(Student.objects.filter(id__in=[5, 1]).values()[1])
#         # print(Student.objects.filter(id__range=[1, 5]).values()[0]['id'])
#         # print(Student.objects.filter(id__isnull=True).values().first())
#         # print(len(Student.objects.filter(name__contains='n').values()))
#         # print(len(Student.objects.filter(gender__startswith='m').values()))
#         # print(len(Student.objects.filter(gender__endswith='e').values()))
#         # print(len(Student.objects.filter(gender__endswith='e').values()[0:5:1]))
#         # for i in Student.objects.filter(name__contains='n').order_by('age').values():
#         #     print(i['age'])
#         # for i in Student.objects.filter(name__contains='n').order_by('-age').values():
#         #     print(i['age'])
#         # for i in Student.objects.filter(name__contains='n').values():
#         #     print(i['age'])
#         # print(Student.objects.count())
#         # print(Student.objects.filter(id=1).exists())  # True
#
#         # for i in Student.objects.values('age').distinct().order_by('age').values():
#         #     print(i['age'])
#         pass
#
# # 外键
# class WJ():
#     # 一对一
#     def one_to_one(self):
#         cls = StuCard.objects.create(
#             name=random.randint(20200901, 20201001),
#             balance=random.randint(1000, 2000),
#             student=Student.objects.get(id=2),
#             )
#
#     # 一对多
#     def one_to_many(self):
#         std_filter = Classes.objects.get(id=6)
#         # std_filter.name = 'C/C++'  # 修改数据
#         # std_filter = Classes.objects.create(name='数据库')
#
#         # std_filter.save()  # save() 会把每个字段都更新一遍
#
#         std = Student.objects.filter(age=20).update(classes=std_filter)
#
#     # 多对多
#     def many_to_many(self):
#         # teach = Teacher.objects.create(name='edgells').classes.add(Classes.objects.get(id=2))
#         # teach = Teacher.objects.get(name='edgells').classes.add(Classes.objects.get(id=2))
#         # 增加数据
#         def create_():
#             cls_list=[]
#             for i in range(10):
#                 cls = Classes.objects.create(
#                     name='cls__new_%s' % i
#                 )
#                 cls_list.append(cls)
#             for n in range(10):
#                 teach = Teacher.objects.create(
#                     name='demo--%s' % n
#                 ).classes.add(*tuple(cls_list))
#
#         # 修改数据
#         def update_():
#             cls_list = []
#             for i in range(10):
#                 cls = Classes.objects.create(
#                     name='cls__new_%s' % i
#                 )
#                 cls_list.append(cls)
#             for n in range(10):
#                 teach = Teacher.objects.filter(
#                     name='demo--%s' % n
#                 ).classes.update(*tuple(cls_list))
#             pass
#
#         # 删除数据
#         def clear_():
#             for n in range(10):
#                 teach = Teacher.objects.filter(
#                     name='demo--%s' % n
#                 ).first().classes.clear()
#
#             # 删除多个，需要拿到两个对象
#             # 从老师里面删除多个班级
#             t = Teacher.objects.get(id=1)
#             clls = t.classes.all()
#             t.classes.remove(clls)
#             Teacher.objects.get(id=1).classes.remove(Teacher.objects.get(id=1).classes.all())
#             pass
#
#         cls1 = Classes.objects.get(id=4)
#         cls2 = Classes.objects.get(id=6)
#         teach = Teacher.objects.get(name='edgells').classes.add(cls1, cls2)
#
#         pass
#
# # orm管理器+事务操作
# class SpuManager_():
#     def Spu_(self):
#         Spu.manager.create(
#             name='奔驰--100',
#             count=10,
#             price=10000,
#         )
#
#     def Order_(self):
#         try:
#             with transaction.atomic():
#                 count = 10
#
#                 bz = Spu.manager.filter(is_del=True, id=2).first()
#
#                 if bz.count < count:
#                     return 0
#
#                 # 订单
#                 bz.count = bz.count - 10
#                 bz.save()
#
#                 # 出现异常
#                 raise Exception("异常出现！！！")
#
#                 Order.objects.create(
#                     name='奔驰--100',
#                     count=10,
#                     total=10 * bz.price
#                 )
#         except Exception as e:
#             transaction.rollback()  # 进行回滚操作
#             print(e)
#
#
# # 聚合查询
# def JH():
#     from django.db import models
#     count_ = Student.objects.count()
#
#
#     std = Student.objects.aggregate(models.Max('age'))  # 最大
#
#     min_age = Student.objects.aggregate(models.Min('age'))     #  最小
#
#     avg_age = Student.objects.aggregate(models.Avg('age'))#  平均
#
#     min_ = Student.objects.aggregate(models.Sum('age'))    #  总和
#
#
# # 分组查询
# def annotate_select():
#     from django.db import models
#     # stds = Student.objects.values('age').annotate(count=Count('age'))
#     d_ = Student.objects.values('age').annotate(models.Count('age'))
#     for i in d_:
#         print(i)
#
#
#
# if __name__ == '__main__':
#     # CDUS().delete_1()
#     # S().select_()
#     # WJ().many_to_many()
#     # SpuManager_().Order_()
#     annotate_select()
#     pass
