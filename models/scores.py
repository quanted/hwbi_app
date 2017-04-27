import copy


class Scores:
    """HWBI Scores Model"""
    def __init__(self):
        self.capitalinvestment = 0.0
        self.consumption = 0.0
        self.employment = 0.0
        self.finance = 0.0
        self.innovation = 0.0
        self.production = 0.0
        self.redistribution = 0.0
        self.airquality = 0.0
        self.foodfiberandfuel = 0.0
        self.greenspace = 0.0
        self.waterquality = 0.0
        self.waterquantity = 0.0
        self.activism = 0.0
        self.communication = 0.0
        self.communityandfaith = 0.0
        self.education = 0.0
        self.emergencypreparedness = 0.0
        self.familyservices = 0.0
        self.healthcare = 0.0
        self.justice = 0.0
        self.labor = 0.0
        self.publicworks = 0.0

    #Get a copy of the dictionary
    def get_dict(self):
        return copy.deepcopy(self.__dict__)

    #def set_dict(self, dict):
    #    self.self.__dict__ = copy.deepcopy(dict)


    def set_dict(self, dct=None):
        if dct is None:
            return
        for attr, value in dct.iteritems():
            attr_lower = attr.lower()
            if attr_lower in self.__dict__:
                self.__dict__[attr_lower] = dct[attr]

    def get_metadata(self):
        lst = []
        for attr, value in self.__dict__.iteritems():
            dct_attr = dict(name=attr, value=value, description='')
            lst.append(dct_attr)

        return lst
