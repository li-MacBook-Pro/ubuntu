from django.urls import path, re_path

from . import views

# app_name = 'apps'

urlpatterns = [
    # path('orm_one/', views.orm_one, name='orm_one'),

    # path('add_s/', views.add_s, name='add_s'),
    # path('s_s/', views.select_s, name='s_s'),
    # path('d/', views.delete, name='d_users'),
    # path('u/', views.update_users, name='u_users'),

    # path('test/', views.static_test, name='test'),

    # path('request/', views.request_test),
    # path('get/', views.get_test),
    # path('post/', views.post_test),

    # path('view/', views.UserApiView.as_view(), name='view'),

    path('uploads/', views.uploads_test),
    # path('set_ck/', views.set_ck),
    # path('get_ck/', views.get_ck),
    # path('del_ck/', views.delete_ck),

    # path('home/', views.home, name='home'),
    # path('login/', views.login1, name='login'),
    # path('logout/', views.logout1, name='logout'),

    path('add_form/', views.add_form, name='add_form'),
    path('register/', views.register, name='register'),
    path('login1/', views.LoginView.as_view(), name='login1'),

    path('', views.T_demo.as_view(), name='li'),

]
