#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
__author__ = 'sunwei'
__mtime__ = 21/03/2018 17:17
__email__ = 'sunwei0325@gmail.com'
"""

from django import forms
from .models import Post

class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('title', 'text',)