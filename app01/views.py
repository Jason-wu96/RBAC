"""
权限组件功能测试
"""

from django.shortcuts import render, HttpResponse,redirect
from rbac.models import *
from rbac.server.permission_session import *

#  登录页面
def login(request):
    if request.method == 'POST':
        username = request.POST.get('user')
        pwd = request.POST.get('pwd')
        user = User.objects.filter(name=username,password=pwd).first()
        if user:
            #注册登陆用户id地址
            request.session['user_id'] = user.pk
            #调用rbac里面的permission_session中的函数
            init_permission(user,request)
            return redirect('/users/')
        else:
            return render(request, 'login.html')
    return render(request,'login.html')

# 查看员工
def users(request):
    user_list = User.objects.all()
    id = request.session['user_id']
    user = User.objects.filter(id = id).first()
    permission_list = request.session.get('permission_list')
    menu_permission = request.session.get("menu_permission")
    return render(request,'users.html',locals())

# 添加员工 （可以用form组件做，但是此处由于辅助测试，简单而过）
def add_user(request):
    return HttpResponse('add')

# 删除员工（由于测试用的没有做的太过仔细）
def delete_users(request,pk):
    return HttpResponse('delete')

# 编辑 （同上）
def edit_users(request,pk):
    return HttpResponse('edit')

# 角色页面
def roles(request):
    role_list = Role.objects.all()
    permission_list = request.session.get('permission_list')
    return render(request,'roles.html', locals())