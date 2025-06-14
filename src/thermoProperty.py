from CoolProp.CoolProp import PropsSI, PhaseSI

class ThermoProperty():
    def __init__(self, name, fluid):
        self.name = name
        self.fluid = fluid

        self.mass_flow_rate = None

        self.T = None
        self.P = None
        self.H = None
        self.S = None
        self.Q = None

        self.resume = None

    def set_mass_flow_rate(self, mass_flow_rate):
        self.mass_flow_rate = mass_flow_rate

    def set_temperature(self, T):
        self.T = T + 273.15

    def set_pressure(self, P):
        self.P = P

    def set_enthalpy(self, H):
        self.H = H

    def set_entropy(self, S):
        self.S = S

    def set_quality(self, Q):
        self.Q = Q

    def calculate(self):
        T_flag = self.T is not None
        P_flag = self.P is not None
        H_flag = self.H is not None
        S_flag = self.S is not None
        Q_flag = self.Q is not None

        if P_flag and T_flag:
            self.H = PropsSI('H', 'P', self.P, 'T', self.T, self.fluid)
            self.S = PropsSI('S', 'P', self.P, 'T', self.T, self.fluid)
            self.resume = (f"--- P = {self.P/1e3} kPa\n"
                           f"--- T = {self.T - 273.15} C\n"
                           f"--- H = {self.H/1e3} kJ/kg\n"
                           f"--- S = {self.S/1e3} kJ/kgK\n")