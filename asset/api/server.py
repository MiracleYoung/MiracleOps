#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/12 下午7:40
# @Author  : MiracleYoung
# @File    : server.py

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..serializer import ServerSerializer
from ..models import Server

__all__ = ['ServerDetailApi']


class ServerDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = ServerSerializer

    def delete(self, request, *args, **kwargs):
        queryset = Server.objects.filter(pk=kwargs.get('pk', ''))
        try:
            queryset.update(status=2)
            return Response('', status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('', status=status.HTTP_502_BAD_GATEWAY)
