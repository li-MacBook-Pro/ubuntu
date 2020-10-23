
from django.http.response import HttpResponse

from django.utils.deprecation import MiddlewareMixin
from orms.models import UserModel


# 主目录下和子app下创建都可以
# 案例1
class MyException(MiddlewareMixin):

    # 执行视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
    def process_request(self, request):
        print('自定义的process_request')
        # request.user = 'li'
        return None

    # 调用视图之前被调用，在每个请求上调用，返回None或HttpResponse对象
    def process_view(self, request, callback, callback_args, callback_kwargs):
        print('自定义的process_view')
        return None

    # 试图函数中函数中的返回值有render方法才会执行process_template_response
    # 在视图刚好执行完毕之后被调用，在每个请求上调用，返回实现了render方法的响应对象
    def process_template_response(self, request, response):
        print('自定义的process_template_response')
        return None

    # 所有响应返回浏览器之前被调用，在每个请求上调用，返回HttpResponse对象
    # def process_response(self, request, response):
    #     print('自定义的process_response')
        # return None

    # 当视图抛出异常时调用，在每个请求上调用，返回一个HttpResponse对象
    def process_exception(self, request, exception):
        print('自定义的process_exception')
        # return HttpResponse(exception)
        return None


# 案例2
class UserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        # request到达之前执行的代码
        username = request.session.get('username', 'user未登录')
        user = UserModel.objects.filter(username=username).first()
        if user:
            setattr(request, 'my_user', user.username)
        else:
            setattr(request, 'my_user', '未登录')
        response = self.get_response(request)
        # response到达用户浏览器之前执行的代码
        return response




