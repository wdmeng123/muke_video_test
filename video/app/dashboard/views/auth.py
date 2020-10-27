# -*- coding: utf-8 -*-

# @File    : auth.py
# @Date    : 2020-10-27
# @Author  : mengwudi

from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate
from app.libs.base_render import render_to_response
from django.shortcuts import redirect


class Login(View):
    template = 'dashboard/auth/login.html'

    def get(self, request):
        data = {'error': ''}
        print(dir(request.user))
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        return render_to_response(request, self.template, data)

    def post(self, request):
        username = request.POST.get('username')
        password = request.POST.get('password')

        exists = User.objects.filter(username=username).exists()
        data = {}
        if not exists:
            data['error'] = '该用户不存在！'
            return render_to_response(request, self.template, data)

        user = authenticate(username=username, password=password)

        if not user:
            data['error'] = '密码错误！！'
            return render_to_response(request, self.template, data)

        if not user.is_superuser:
            data['error'] = '您无权登录管理员页面！'
            return render_to_response(request, self.template, data)
        login(request, user)
        return redirect('/dashboard/')
