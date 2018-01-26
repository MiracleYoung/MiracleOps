#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 1/26/18 4:28 PM
# @Author  : Miracle Young
# @File    : str_parse.py

def text2html(s: str):
    return s.replace('\n', '<br>').replace(' ', '&nbsp;')