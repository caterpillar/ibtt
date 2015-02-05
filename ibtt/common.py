# coding=utf-8
__author__ = 'lishaohua'

import json
from django.http import HttpResponse


class Json:
    _content_type = 'application/json'
    data = {}

    def __init__(self, data=None):
        if data is not None and not isinstance(data, dict):
            raise ValueError('data is not dict')
        self.data['data'] = data

    def put(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def http_response(self, success=None, msg=None):
        """
        返回一个application/json类型的包含data数据的(如果有)HttpResponse,
        :param success:默认为True,标志请求是否成功
        :param msg:返回客户端的消息
        :return: HttpResponse
        """
        if success is None:
            success = True
        self.data['success'] = success
        if msg is not None:
            self.data['msg'] = msg
        else:
            if success:
                self.data['msg'] = 'success'
            else:
                self.data['msg'] = 'failed'
        json_str = json.dumps(self.data)
        return HttpResponse(json_str, self._content_type)
