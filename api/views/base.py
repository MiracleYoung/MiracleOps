#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 3/5/18 3:18 PM
# @Author  : Miracle Young
# @File    : base.py


from rest_framework import views, response


class BaseAPIView(views.APIView):
    def json_response(self, code, data, msg):
        return response.Response(data={'code': code, 'data': data, 'msg': msg}, status=code,
                                 content_type='application/json')
