# coding=utf-8
__author__ = 'lishaohua'

from django import forms


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField()


class RegisterBaseInfo(forms.Form):
    username = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()