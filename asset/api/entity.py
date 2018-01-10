#!/usr/bin/env python
# encoding: utf-8
# @Time    : 2018/1/9 下午10:13
# @Author  : MiracleYoung
# @File    : entity.py

from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import status
from ..serializer import EntitySerializer
from ..models import Entity

__all__ = ['EntityDetailApi']

class EntityDetailApi(RetrieveUpdateDestroyAPIView):
    serializer_class = EntitySerializer
    queryset = Entity.objects.all()

    def get_queryset(self):
        queryset = super(EntityDetailApi, self).get_queryset()
        return queryset

    def delete(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        try:
            queryset.update(status=2)
            return Response('', status=status.HTTP_204_NO_CONTENT)
        except:
            return Response('', status=status.HTTP_502_BAD_GATEWAY)


