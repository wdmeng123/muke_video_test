# coding:utf-8

from django.views.generic import View
from app.libs.base_render import render_to_response


class Base(View):
    TEMPLATE = 'dashboard/base.html'

    def get(self, request):
        print('test2')

        render_to_response(request, self.TEMPLATE)