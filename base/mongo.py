__author__ = 'lishaohua'
# encoding='utf8'
from pymongo import Connection
from bson.objectid import ObjectId
import gridfs
import threading


class GridFS:
    connection = None
    database = None
    file_system = None
    instance = None
    locker = threading.locker()

    @staticmethod
    def _connect():
        if not GridFS.connection:
            GridFS.connection = Connection("mongodb://admin:admin@127.0.0.1:27017")
        GridFS.database = GridFS.connection['ib_core']


    def __init__(self):
        GridFS._connect()


    @staticmethod
    def get_instance():
        GridFS.locker.acquire()
        try:
            if not GridFS.instance:
                GridFS.instance = GridFS()
            return GridFS.instance
        finally:
            GridFS.locker.release()


    def save(self, collection='fs', data=None):
        if not data:
            raise ValueError('data is null')
        GridFS.file_system = gridfs.GridFS(GridFS.database, collection=collection)
        GridFS.file_system.put()


    def get(self, collection='fs', object_id=None):
        if not id:
            return ValueError('id is null')
        GridFS.file_system = gridfs.GridFS(GridFS.database, collection=collection)
        return GridFS.file_system.get(ObjectId(object_id))