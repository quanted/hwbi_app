import copy
from datetime import datetime
import json

version = 1.0


class MetaBase():
    """MetaBase class"""
    def __init__(self, name='', value='', description=''):
        self.name = name
        self.value = value
        self.description = description

    def get_dict(self):
        return copy.deepcopy(self.__dict__)


class MetaInput():
    """MetaInput class"""
    def __init__(self, name='', description = '', min=0.0, max=0.0,unit='', type='', required=False):
        self.name = name
        self.description = description
        self.min = min
        self.max = max
        self.unit = unit
        self.type = type
        self.required = required

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
        self.modelVersion = model
        self.collection = collection
        self.version = version
        self.description = ""
        self.status = ""
        self.timestamp = str(datetime.now())
        self.url = Url()

    def get_dict(self):
        dct = copy.deepcopy(self.__dict__)
        dct['url'] = self.url.get_dict()
        return dct


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