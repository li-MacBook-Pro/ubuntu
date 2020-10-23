from django.contrib import admin

# Register your models here.

from orms.models import Users, Department, Student, UserModel


# 定义管理
class OrderAdmin(admin.ModelAdmin):
    list_per_page = 10  # 调整每页显示多少条数据
    # 字段可以是列和方法  # 模型字段是数据库内字段  '__str__'
    # list_display = ['id', 'name', 'total', 'total_count']
    search_fields = ['name']  # 根据字段搜索
    list_filter = ['name']  # 根据字段过滤结果集 过滤框会出现在右侧
    # models内操纵short_description  # 更改显示名字，
    admin_order_field = '模型类字段'  # 模型类字段
    admin_on_top = True  # 动作在顶部还是地步
    admin_in_bottom = False  # 动作在顶部还是底步


class UsersAdmin(admin.ModelAdmin):
    actions_on_top = True  # 动作在顶部还是底部
    list_per_page = 10  # 调整每页显示多少条数据
    # 字段可以是列和方法
    # 模型字段是数据库内字段,给'classes'重新命名  self.classes.name
    list_display = ['id', 'name', 'age', ]
    search_fields = ['name']  # 根据字段搜索
    list_filter = ['name']  # 根据字段过滤结果集
    admin_order_field = ['age']  # 方法列不能直接排序
    actions_on_bottom = True  # 动作在顶部还是底部

    # 修改界面 fields：属性的先后顺序 fieldsets：属性分组 二者选一
    # fields = ['age', 'name', ]  # 此处不能用
    fieldsets = (
        ('基本', {'fields': ['name']}),
        ('扩展', {'fields': ['gender', 'age']}),
    )


# 以快嵌入
class TestBlockStackInline(admin.StackedInline):
    model = 'li'  # model = '模型类'
    extra = 1  # extra = 1附加的编辑类


# class TestAdmin(admin.ModelAdmin):
#     inlines = ['TestBlockStackInline', ]


# 以表格形式：
# class TestTabularInline(admin.TabularInline):
#     model = '模型类'
#     extra = 1


class TestAdmin(admin.ModelAdmin):
    inlines = ['testBlockStackInline', ]
    # inlines = ['TestBlockStackInline', ]


# @admin.register(UserModel)
# class UserAdmin(admin.ModelAdmin):
#     pass


# 调整站点信息：
# admin.site.site_header = '设置网站页头'
# admin.site.site_title = '设置网站标题'
# admin.site.index_title = '设置首页标语'

admin.site.register(UserModel)
# admin.site.register(Users, UsersAdmin)

# admin.site.register()



