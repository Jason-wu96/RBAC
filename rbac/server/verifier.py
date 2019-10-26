"""
登录验证中间件
"""

from django.utils.deprecation import MiddlewareMixin
import re
from django.shortcuts import HttpResponse,redirect


class PermissionMiddleware(MiddlewareMixin):

    def process_request(self,request):
        current_path = request.path_info
        # 白名单
        white_list = ['/login/', '/admin/.*']
        for _url in white_list:
            ret = re.match(_url, current_path)
            if ret:
                return None
        # 如果没有登录返回登录页面
        user_id = request.session.get('user_id')
        if not user_id:
            return redirect('/login/')
        flag = False
        permission_list = request.session.get('permission_list', [])
        for permission in permission_list:
            permission = "^%s$" % permission
            ret = re.match(permission, current_path)
            if ret:
                flag = True
                break
        if not flag:
            return HttpResponse('无权访问')




