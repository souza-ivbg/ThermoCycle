from .equipment import Equipment


class Turbine(Equipment):
    def __init__(self, name):
        super().__init__(name)
        self.heat = 0.0

    def calculate(self):
        self.work = - self.enthalpy_balance