

class Retailitem:
    def __init__(self):
        self.description = 0
        self.unit = 0
        self.price_per_unit = 0
    def descript(self,value):
        self.description = value
    def units(self,value):
        self.unit = value
    def price(self,value):
        self.price_per_unit = value
    def get_descript(self):
        return self.description
    def get_units(self):
        return self.unit
    def get_price(self):
        return self.price_per_unit