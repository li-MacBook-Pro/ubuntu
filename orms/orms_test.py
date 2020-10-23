
import os
import random
import sys

import django

from django.db import transaction  # django事务

# from orms.models import Users, Student, Department  # 导入自定义的模型类

from django.db.models import Max, Min, Sum, Count, Avg
from django.db.models import Q, F

# 准备django 目录 并插入解释寻包路径

project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程目录
sys.path.insert(0, project)

# 载入django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django21.settings')

django.setup()


from orms.models import Users, Student, Department, UserModel, ip  # 导入自定义的模型类


class Test():

    def create(self, id, name, d_id):

        # Department.objects.create(d_id=id, d_name=name).save()
        # Student.objects.create(s_id=id, s_name=name, departments_id=d_id).save()
        UserModel.objects.create(username=id, password=name, email=d_id).save()

    def select(self, name):
        try:

            s = Student.objects.filter(departments__d_id=name)

            c = Department.objects.get(d_id=1)
            # s = Student.objects.all().filter(departments=c)

            # user = Student.objects.get(
            #     id=name,
            # )  # get例如：名字相同的有两个，这样获取就会报错；查询不存在的数据也会报错。
            # print('id={}：name={}'.format(name, user.name))
            # print(s.name)
            # print(s)

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
            return s
        except Users.DoesNotExist as e:
            print(e)

    def delete_db_data(self):
        try:
            ip.objects.get(id=2).delete()
            ip.objects.get(id=19).delete()
            ip.objects.get(id=20).delete()
            print('del')
        except ip.DoesNotExist as e:
            print(e)


if __name__ == '__main__':
    #
    # Test().create('li', 'password', False)
    # Test().create(1, 'li', 1)
    # Test().create('li', 'password', 'li1999092966@gmail.com')

    # Test().select(1)
    Test().delete_db_data()

    pass
