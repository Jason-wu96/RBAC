# 查看当前登录用户的所有权限
def init_permission(user, request):
    permissions = user.roles.all().values("permissions__url").distinct()
    permission_list = []
    for item in permissions:
        permission_list.append(item['permissions__url'])

    request.session['permission_list'] = permission_list

    # 菜单权限注册
    permission = user.roles.all().values("permissions__url", "permissions__action", "permissions__group__title").distinct()
    menu_permission = []
    for item in permission:
        if item['permissions__action'] == 'list':
            temp = (item['permissions__url'],item['permissions__group__title'])
            print(temp)
            menu_permission.append(temp)
            print(menu_permission)
    request.session['menu_permission'] = menu_permission





