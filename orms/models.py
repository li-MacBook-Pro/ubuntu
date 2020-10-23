
from django.db import models

# Create your models here.


class Users(models.Model):
    # CHOICES_GENDER = ((0, 'null'))
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1024, verbose_name='姓名代号', default='0')
    # gender = models.BooleanField(max_length=255, choices=CHOICES_GENDER, default='o', verbose_name='性别')
    age = models.CharField(max_length=10, null=True, verbose_name='年龄')

    # in_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    # class Meta:
    #     # db_table = 'users'  # 指定数据库表单
    #     ordering = ['age']  # 在Django层面升序降序排列，可以不用再模版里写

    # def __str__(self):
    #     return 'Users<id=%s,name=%s,gender=%s,age=%s>' % (
    #         self.id, self.name, self.age, self.gender,
    #     )


class Department(models.Model):

    d_id = models.AutoField(primary_key=True)
    d_name = models.CharField(max_length=20, verbose_name='学院名称')

    # in_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    class Meta:
        db_table = 'orm_department'

    def __str__(self):
        return self.d_name


class Student(models.Model):

    s_id = models.AutoField(primary_key=True)
    s_name = models.CharField(max_length=30, verbose_name='姓名代号')

    # in_delete = models.BooleanField(default=False, verbose_name='逻辑删除')

    departments = models.ForeignKey('Department', related_name='student', on_delete=models.CASCADE)

    class Meta:
        db_table = 'orm_student'

    def __str__(self):
        return self.s_name


class UserModel(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    class Meta:
        db_table = 'orm_UserModel'


class Obtain_1(models.Model):
    ip = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    l_l = models.CharField(max_length=50)
    radius = models.CharField(max_length=50)
    postal = models.CharField(max_length=50)

    class Meta:
        db_table = 'orm_Obtain_1'


class Obtain_2(models.Model):
    ip = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    l_l = models.CharField(max_length=50)
    radius = models.CharField(max_length=50)
    postal = models.CharField(max_length=50)

    class Meta:
        db_table = 'orm_Obtain_2'


class ip(models.Model):
    ip = models.CharField(max_length=30)
    number = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    l_l = models.CharField(max_length=50)
    radius = models.CharField(max_length=50)
    postal = models.CharField(max_length=50)
    create_at = models.DateTimeField(auto_now_add=True, null=True)
    update_at = models.DateTimeField(auto_now=True, null=True)

    # def __str__(self):
    #     return 'ip<id=%s,number=%s,address=%s,l_l=%s>' % (
    #         self.ip, self.number, self.address, self.l_l,
    #     )
