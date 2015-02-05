# coding=utf-8

__author__ = 'lishaohua'

from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from baby.forms import LoginForm
from ibtt.common import Json


def home(request):
    return render_to_response('home.html')

# Create your views here.


def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            login_info = form.cleaned_data
            user = auth.authenticate(username=login_info.get('username'), password=login_info.get('password'))
            if user is not None:
                return Json().http_response()
            else:
                return Json().http_response(success=False, msg='用户名或密码不正确')
    return Json().http_response(success=False, msg="请求错误,get方法不允许")


def logout(request):
    auth.logout(request)
    return Json().http_response()