# coding=utf-8

__author__ = 'lishaohua'

import logging

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render_to_response
from django.contrib import auth
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.db import transaction
from django.core.mail import send_mail, EmailMultiAlternatives
from base.forms import LoginForm, RegisterBaseInfo
from base.utils import Md5Util
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
                logging.info("id:%, username:& login system" % (user.id, user.username))
                return Json().http_response()
            else:
                return Json().http_response(success=False, msg='用户名或密码不正确')
    return Json().http_response(success=False, msg="请求错误,get方法不允许")


def logout(request):
    auth.logout(request)
    return Json().http_response()


@csrf_exempt
@transaction.atomic
def register_base_info(request):
    if request.method == 'POST':
        # return Json().http_response()  #TODO test
        base_info_form = RegisterBaseInfo(request.POST)
        if base_info_form.is_valid():
            base_info = base_info_form.cleaned_data
            find_users = User.objects.filter(username=base_info['username'])
            if find_users:
                return Json().http_response(success=False, msg='您注册的用户名重复, 请修改后重新注册')
            find_users = User.objects.filter(email=base_info['email'])
            if find_users:
                return Json().http_response(success=False, msg='您的邮箱已经注册过,请换一个邮箱试试或者用已有的账号登录')
            password_md5 = Md5Util.md5(base_info['password'])
            user = User(username=base_info['username'], email=base_info['email'], password=password_md5,
                        is_active=False)
            user.save()
            _send_reg_activate_mail(user)
            logging.info("username % register success, input base info" % user.username)
            return Json().http_response()
        else:
            return Json(base_info_form.errors).http_response(success=False, msg="参数校验不合法")
    return Json().http_response(success=False, msg="请求错误,get方法不允许")


def email_activate(request, username, activate_code):
    if username is None:
        pass
    if activate_code is None:
        pass
    find_users = User.objects.filter(username=username)
    if find_users:
        return Json().http_response(success=False, msg='用户不存在')
    activate_user = find_users.get(0)
    password = activate_user.password
    if activate_code == Md5Util.md5(password):
        activate_user.update(is_active=True)
        return Json().http_response(msg="激活成功")
    else:
        return Json().http_response(success=False, msg="激活失败")



def _mail_content(user):
    html_content = u'%s,您好:<br/>' % user.username
    html_content += u'&nbsp;&nbsp;您需要点击超链接激活您的邮件:<a href="http://localhost:8000/email_activate/%s/%s">这里</a>' % (
        user.username, Md5Util.md5(user.password))
    return html_content


def _send_reg_activate_mail(user):
    subject, mail_from, mail_to = '来自爱宝天天的账号激活邮件', 'ibabyeveryday@126.com', [user.email]
    # send_mail(subject, mail_content(), mail_from, mail_to, fail_silently=True)
    text_content = 'This is an important message'
    msg = EmailMultiAlternatives(subject, text_content, mail_from, mail_to)
    msg.attach_alternative(_mail_content(user), 'text/html')
    msg.send()