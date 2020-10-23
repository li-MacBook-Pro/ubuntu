
import os
import sys
import pathlib

import django


project = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # 工程目录
sys.path.insert(0, project)

# 载入django 环境
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django21.settings')

django.setup()


path = pathlib.Path("/Users/li/Library/Mobile Documents/com~apple~CloudDocs/Django/django/static/image")
# print(dir(path))
print("展示文件夹名：")
print(path.name)
print("展示整个路径：")
print(path)

# print("\n展示直接下级:")
# for i in path.iterdir():
#     print(i)
# print("遍历所有下级:")
# for i in path.glob("**/*"):
#     print(i)
