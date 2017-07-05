# import copy
#
#
# class DomainWeights:
#     """HWBI Domain Weights Model"""
#     def __init__(self):
#         self.connectiontonature = 1.0
#         self.culturalfulfillment = 1.0
#         self.education = 1.0
#         self.health = 1.0
#         self.leisuretime = 1.0
#         self.livingstandards = 1.0
#         self.safetyandsecurity = 1.0
#         self.socialcohesion = 1.0
#
#     def get_dict(self):
#         return copy.deepcopy(self.__dict__)
#
#     def set_dict(self, dct=None):
#         if dct is None:
#             return
#         for attr, value in dct.iteritems():
#             attr_lower = attr.lower()
#             if attr_lower in self.__dict__:
#                 self.__dict__[attr_lower] = dct[attr]
#
#     def get_metadata(self):
#         lst = []
#         for attr, value in self.__dict__.items():
#             dct_attr = dict(name=attr, value=value, description='')
#             lst.append(dct_attr)
#
#         return lst
