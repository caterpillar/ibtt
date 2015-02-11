# coding=utf-8

__author__ = 'lishaohua'

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from base.forms import LoginForm, RegisterBaseInfo
from ibtt.common import Json


def home(request):
    return render_to_response('home.html')


# Create your views here.


@csrf_exempt
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

@csrf_exempt
def register_base_info(request):
    if request.method == 'POST':
        return Json().http_response()  #TODO temp
        base_info_form = RegisterBaseInfo(request.POST)
        if base_info_form.is_valid():
            base_info = base_info_form.cleaned_data
            user = User(username=base_info['username'], email=base_info['username'], password=base_info['password'])
            user.save()
            print(user.id)
            return Json().http_response()
        else:
            return Json(base_info_form.errors).http_response(success=False, msg="参数校验不合法")
    return Json().http_response(success=False, msg="请求错误,get方法不允许")


