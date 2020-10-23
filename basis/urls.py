from django.urls import path, re_path

from . import views


urlpatterns = [
    path('index/<str:xx>/', views.one, name='old'),
    re_path('^index/$', views.two),
    path('index/new_version/', views.three, name='new_version'),
    path('html/', views.four),
    path('label/', views.seven),
    path('inherit/', views.eight, name='inherit'),
    path('custom/', views.custom, name='custom'),
    path('nine/', views.nine),
    path('thirteen/', views.thirteen, name='thirteen'),

]