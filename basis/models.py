from django.db import models

# Create your models here.


class Users(models.Model):
    # id = models.AutoField(primary_key=True)  # Django自动加上
    CHOICES_GENDER = ((0, 'null'),)

    name = models.CharField(max_length=1024, verbose_name='姓名代号', default='0')
    gender = models.BooleanField(max_length=255, choices=CHOICES_GENDER, default='o', verbose_name='性别')
    age = models.IntegerField(max_length=10, null=True, verbose_name='年龄')

    def __str__(self):
        return 'User<id=%s,name=%s,gender=%s,age=%s>' % (
            self.id, self.name, self.gender, self.age
        )


class Department(models.Model):

    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=20, verbose_name='学院名称')

    class Meta:
        db_table = 'orm_department'

    def __str__(self):
        return self.d_name


class Student(models.Model):

    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30, verbose_name='姓名代号')

    departments = models.ForeignKey('Department', related_name='student', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orm_student'

    def __str__(self):
        return self.s_name

# class Student(models.Model):
#     name = models.CharField(max_length=255, null=True, verbose_name='学生姓名')
#     gender = models.CharField(max_length=255, verbose_name='性别', null=True,)
#     birthday = models.DateField(verbose_name='生日', null=True,)
#     age = models.IntegerField(null=True)
#     phone = models.CharField(max_length=11, null=True, verbose_name='手机号')
#
#     create_at = models.DateTimeField(auto_now_add=True, null=True)
#     update_at = models.DateTimeField(auto_now=True, null=True)
#
#     #  关系
#     #  一对多：一个班级多个学生
#
#     classes = models.ForeignKey('Classes', on_delete=models.SET_NULL, null=True, related_name='Classes')
#
# #
#     #  Django代替数据库操作
#
#     class Meta:
#         # db_table = 'darabase_1'  # 指定数据库表单
#         ordering = ['age']  # 在Django层面升序降序排列，可以不用再模版里写


# # 一对多：一个班级多个学生
# class Classes(models.Model):
#     name = models.CharField(max_length=255, null=True, verbose_name='班级名称')
#
#
# # 一对一：一个学生一张饭卡
# class StuCard(models.Model):
#     name = models.CharField(max_length=255, null=True, verbose_name='饭卡名称')
#     balance = models.IntegerField(default=0, verbose_name='余额')
#
#     #  关系
#     #  一对一：一个学生一张饭卡
#     student = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='card')
#
#
# # 多对多：老师拥有多个学生多个班级、班级有多个老师、学生有多个老师
# class Teacher(models.Model):
#     name = models.CharField(max_length=255, null=True, verbose_name='老师姓名')
#
#     #  关系
#     #  多对多：老师拥有多个学生多个班级、班级有多个老师、学生有多个老师
#     classes = models.ManyToManyField(Classes, related_name='teacher', verbose_name='老师-->班级')


# orm管理器案例：
# 下单
# class Order(models.Model):
#     name = models.CharField(max_length=255, null=True, verbose_name='标题')
#     count = models.IntegerField(default=0, verbose_name='数量')
#     total = models.IntegerField(default=0, verbose_name='总计')
#
#     # admin操作
#     # 添加
#     def total_count(self):
#         return f'id--{self.total}'
#     # 更改显示名字
#     total_count.short_description = '总计'
#
#
#
# # orm管理器
# class SpuManager(models.Manager):
#
#     def all(self):
#         return super().filter(is_del=True, is_show=True)  # 返回查询集
#
# # 库存
# class Spu(models.Model):
#     name = models.CharField(max_length=255, null=True, verbose_name='名称')
#     count = models.IntegerField(default=0, verbose_name='数量')
#     price = models.IntegerField(default=0, verbose_name='单价')
#     is_show = models.BooleanField(default=True)  # 数据展示
#     is_del = models.BooleanField(default=True)  # 数据存在
#     manager = SpuManager()  # 实例化
#
#     def __str__(self):
#         return self.name
#
#
# def app(environ, start_response):
#     start_response('200 OK', [('Content-Type', 'text/plain')])
#     yield "Hello world!\n"
#
#
# # 小案例