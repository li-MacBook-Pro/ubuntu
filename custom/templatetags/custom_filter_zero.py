import datetime

import time

# from . import register
from django import template

register = template.Library()


# @register.filter
def my_cut(value, arg):
    return value.replace(arg, '')


register.filter('my_cut_zero', my_cut)


@register.filter
def my_upper(value, *args):
    return value.upper()


@register.filter
def my_lower(value, *args):
    return value.lower()


@register.simple_tag
def show_name(name):
    return name


@register.simple_tag
def current_time(format_str):
    return datetime.datetime.now().strftime(format_str)


@register.simple_tag(takes_context=True)
def current_time_0(context):
    return datetime.datetime.now().strftime(context.get('format_str'))


@register.simple_tag(takes_context=True)
# 简单过滤器  takes_context表示是否取views.py传递过来的参数.如果等于True,则取，否则则不取。
def current_time_1(context, format_string):  # 此方法是格式化显示当前时间，具体介绍请百度参照python的time模块。
    # return datetime.datetime.now().strftime(context.get('format_str'))
    return [
        datetime.datetime.now().strftime(context.get(format_string)),
        time.strftime(format_string, time.localtime()),
    ]


@register.inclusion_tag('html/custom/filter_one.html', name='stags')
def show_tags(person, person1,):

    items = [{
            'name': 'li',
            'age': '18',

    }]
    return {'items': items,
            'person': person,
            'person1': person1,
            }


@register.inclusion_tag('html/custom/filter_zero.html',)
def new_tags():
    return {
        'choices': ['python'],
    }