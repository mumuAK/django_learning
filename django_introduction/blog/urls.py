#!/usr/bin/env python
# -*- coding:utf-8 -*-
#@Time  : 2020/3/15 14:32
#@Author: mumu Wang
#@File  : urls.py

from django.urls import path,include

import blog.views

urlpatterns = [
    path('hello_world', blog.views.hello_world),
    path('content', blog.views.article_content),
    path('index', blog.views.get_index_page),
    #path('detail', blog.views.get_detail_page),
    path('detail/<int:article_id>', blog.views.get_detail_page),
]