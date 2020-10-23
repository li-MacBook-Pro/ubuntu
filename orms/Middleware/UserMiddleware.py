

from orms.models import UserModel


# 案例2
class UserMiddleware(object):
    def __init__(self, get_response):
        self.get_response = get_response
        # super().__init__()

    def __call__(self, request):
        # response = None
        # request到达之前执行的代码
        username = request.session.get('username', '未登录')
        user = UserModel.objects.filter(username=username).first()
        if user:
            setattr(request, 'my_user', user.username)
        else:
            setattr(request, 'my_user', '未登录')
        response = self.get_response(request)

        # response到达用户浏览器之前执行的代码
        return response