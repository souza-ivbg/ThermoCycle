from src.thermoProperty import ThermoProperty
from src.connector import Connector
from src.equipment.turbine import Turbine
from src.equipment.heater import Heater
from src.equipment.condenser import Condenser
from src.equipment.pump import Pump
from src.thermoCycle import ThermoCycle

fluid = "Water"
water_mass_flow_rate = 1.0  # kg/s

prop_1 = ThermoProperty("point_1", fluid)
prop_1.set_mass_flow_rate(water_mass_flow_rate)
prop_1.set_pressure(17e3)
prop_1.set_temperature(30)

prop_2 = ThermoProperty("point_2", fluid)
prop_2.set_mass_flow_rate(water_mass_flow_rate)
prop_2.set_pressure(3e6)
prop_2.set_temperature(30)

prop_3 = ThermoProperty("point_3", fluid)
prop_3.set_mass_flow_rate(water_mass_flow_rate)
prop_3.set_pressure(3e6)
prop_3.set_temperature(350)

prop_4 = ThermoProperty("point_4", fluid)
prop_4.set_mass_flow_rate(water_mass_flow_rate)
prop_4.set_pressure(20e3)
prop_4.set_temperature(65)

pipe_1 = Connector("pipe_1")
pipe_1.set_properties_in(prop_3)
pipe_1.set_properties_out(prop_3)

pipe_2 = Connector("pipe_2")
pipe_2.set_properties_in(prop_4)
pipe_2.set_properties_out(prop_4)

pipe_3 = Connector("pipe_3")
pipe_3.set_properties_in(prop_1)
pipe_3.set_properties_out(prop_1)

pipe_4 = Connector("pipe_4")
pipe_4.set_properties_in(prop_2)
pipe_4.set_properties_out(prop_2)

heater = Heater("heater")
turbine = Turbine("turbine")
condenser = Condenser("condenser")
pump = Pump("pump")

heater.add_connectors_in(pipe_4)
heater.add_connectors_out(pipe_1)

turbine.add_connectors_in(pipe_1)
turbine.add_connectors_out(pipe_2)

condenser.add_connectors_in(pipe_2)
condenser.add_connectors_out(pipe_3)

pump.add_connectors_in(pipe_3)
pump.add_connectors_out(pipe_4)

rankine_power_cycle = ThermoCycle()
rankine_power_cycle.add_equipment(pump)
rankine_power_cycle.add_equipment(turbine)
rankine_power_cycle.add_equipment(condenser)
rankine_power_cycle.add_equipment(heater)

rankine_power_cycle.initialize()
rankine_power_cycle.calculate()
rankine_power_cycle.calculate_efficiency()
rankine_power_cycle.draw("app_aula.png")
