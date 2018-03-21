#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
__author__ = 'sunwei'
__mtime__ = 15/03/2018 17:21
__email__ = 'sunwei0325@gmail.com'
"""
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.post_list, name='post_list'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.post_detail, name='post_detail'),
]