import copy
from datetime import datetime
import json

version = 1.0


class MetaBase():
    """MetaBase class"""
    def __init__(self):
        self.name = ""
        self.value = ""
        self.description = ""

    def get_dict(self):
        return copy.deepcopy(self.__dict__)


class MetaInput():
    """MetaInput class"""
    def __init__(self):
        self.name = ""
        self.description = ""
        self.min = 0.0
        self.max = 0.0
        self.unit = ""
        self.type = ""
        self.required = False

    def get_dict(self):
        return copy.deepcopy(self.__dict__)


class MetaOutput:
    """MetaOutput class"""
    def __init__(self):
        self.name = ""
        self.description = ""
        self.min = 0.0
        self.max = 0.0
        self.unit = ""
        self.type = ""

    def get_dict(self):
        return copy.deepcopy(self.__dict__)


class MetaInfo:
    """MetaInfo class"""
    def __init__(self, model='hwbi', collection='qed'):
        self.model = model
        self.collection = collection
        self.version = version
        self.description = ""
        self.status = ""
        self.timestamp = str(datetime.now())
        self.url = Url()

    def get_dict(self):
        return copy.deepcopy(self.__dict__)


class Url:
    """Url class"""
    def __init__(self, href='', type='application/json'):
        self.type = type
        self.href = href

    def get_dict(self):
        return copy.deepcopy(self.__dict__)


class Link:
    """Link class"""
    def __init__(self, rel='', href='', type='application/json'):
        self.rel = rel
        self.type = type
        self.href = href

    def get_dict(self):
        return copy.deepcopy(self.__dict__)


class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if hasattr(obj, 'get_dict'):
            return obj.get_dict()
        else:
            return json.JSONEncoder.default(self, obj)