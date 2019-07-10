import os
ip = input("你的外网IP：")
post = input("你的端口: ")
code = "python manage.py runserver "+ip+":"+post
os.system(code)