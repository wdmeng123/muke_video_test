# -*- coding: utf-8 -*-

# @File    : auth.py
# @Date    : 2020-10-27
# @Author  : mengwudi

from django.views.generic import View
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from app.libs.base_render import render_to_response
from django.shortcuts import redirect, reverse
from django.core.paginator import Paginator


class Login(View):
    template = 'dashboard/auth/login.html'

    def get(self, request):
        data = {'error': ''}
        if request.user.is_authenticated:
            return redirect('/dashboard/')
        return render_to_response(request, self.template, data=data)

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
            return render_to_response(request, self.template, data=data)

        if not user.is_superuser:
            data['error'] = '您无权登录管理员页面！'
            return render_to_response(request, self.template, data=data)
        login(request, user)
        return redirect('/dashboard/')


class Logout(View):

    def get(self, request):
        logout(request)
        return redirect(reverse('dashboard_login'))


class AdminManager(View):
    template = 'dashboard/auth/admin.html'

    def get(self, request):
        # users = User.objects.filter(is_superuser=True)
        users = User.objects.all()
        page = request.GET.get('page', 1)
        p = Paginator(users, 1)
        total_page = p.num_pages
        current_page = p.get_page(int(page)).object_list
        if int(page) <= 1:
            page = 1
        data = {'users': current_page, 'total': total_page, 'page_num': int(page)}
        return render_to_response(request, self.template, data=data)


class UpdateAdminStatus(View):

    def get(self, request):
        status = request.GET.get('status', 'on')
        _status = True if status == 'on' else False
        request.user.is_superuser = _status
        request.user.save()

        return redirect(reverse('admin_manager'))
