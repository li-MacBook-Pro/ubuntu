# import pymysql
#
# conn = pymysql.connect(
#     user='root',
#     password='qwe123',
#     db='demo'
# )
#
# with conn.cursor() as cs:
#     cs.execute("create table user(id int primary key not null);")
# z


import sys, django
sys.path = sys.path[1:]
print(django.__path__)
