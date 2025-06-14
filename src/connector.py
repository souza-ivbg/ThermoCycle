class Connector():
    def __init__(self, name):
        self.name = name
        self.property_in = None
        self.property_out = None
        self.equipment_in = None
        self.equipment_out = None

    def add_equipment_in(self, equipment):
        self.equipment_in = equipment

    def add_equipment_out(self, equipment):
        self.equipment_out = equipment


    def set_properties_in(self, property):
        self.property_in = property

    def set_properties_out(self, property):
        self.property_out = property


    def calculate(self):
        self.property_in.calculate()
        self.property_out.calculate()