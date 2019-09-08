from django.utils.deprecation import MiddlewareMixin
import re
from django.shortcuts import HttpResponse,redirect


class PermissionMiddleware(MiddlewareMixin):

    def process_request(self,request):
        current_path = request.path_info
        white_list = ['/login/', '/admin/.*']
        for _url in white_list:
            ret = re.match(_url, current_path)
            if ret:
                return None

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


