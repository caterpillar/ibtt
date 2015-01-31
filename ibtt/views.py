# coding=utf-8

__author__ = 'lishaohua'

from django.shortcuts import render_to_response


def home(request):
    return render_to_response('home.html')