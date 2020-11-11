# -*- coding: utf-8 -*-

# @File    : permission.py
# @Date    : 2020-11-11
# @Author  : mengwudi

import functools

from django.shortcuts import redirect, reverse


def dashboard_auth(func):
    @functools.wraps(func)
    def wrapper(self, request, *args, **kwargs):

        user = request.user

        if not user.is_authenticated or user.is_superuser:
            return redirect('{}?to={}'.format(reverse('dashboard_login'), request.path))

        return func(self, request, *args, **kwargs)

    return wrapper