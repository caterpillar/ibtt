import types

__author__ = 'lishaohua'
from hashlib import md5


class Md5Util:
    def __init__(self):
        pass

    @staticmethod
    def md5(string):
        if isinstance(string, types.StringType):
            m = md5()
            m.update(string)
            return m.hexdigest()
        else:
            return ''