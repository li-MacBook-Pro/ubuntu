

from orms.models import UserModel


def my_user(request):
    username = request.session.get('user', 'user未登录')
    user = UserModel.objects.filter(username=username).first()
    if user:
        return {'my_user': username}
    else:
        return {}