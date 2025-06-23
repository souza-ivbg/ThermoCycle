from src.thermoProperty import ThermoProperty
from src.equipment.heat_exchanger import HeatExchanger
from src.equipment.mixing_chamber import MixingChamber
from src.connector import Connector
from src.equipment.turbine import Turbine
from src.equipment.heater import Heater
from src.equipment.condenser import Condenser
from src.equipment.pump import Pump
from src.thermoCycle import ThermoCycle


pipe_1 = Connector("pipe_1")
pipe_2 = Connector("pipe_2")
pipe_3 = Connector("pipe_3")
pipe_4 = Connector("pipe_4")
pipe_5 = Connector("pipe_5")
pipe_6 = Connector("pipe_6")
pipe_7 = Connector("pipe_7")
pipe_8 = Connector("pipe_8")
pipe_9 = Connector("pipe_9")

heater = Heater("heater")
turbine = Turbine("turbine")
condenser = Condenser("condenser")
pump_1 = Pump("pump_1")
pump_2 = Pump("pump_2")
heat_exchanger = HeatExchanger("heat_exchanger")
mixing_chamber = MixingChamber("mixing_chamber")

heater.add_connectors_in(pipe_5)
heater.add_connectors_out(pipe_6)

turbine.add_connectors_in(pipe_6)
turbine.add_connectors_out(pipe_7)
turbine.add_connectors_out(pipe_8)

condenser.add_connectors_in(pipe_8)
condenser.add_connectors_out(pipe_1)

pump_1.add_connectors_in(pipe_1)
pump_1.add_connectors_out(pipe_2)

heat_exchanger.add_connectors_in(pipe_2)
heat_exchanger.add_connectors_out(pipe_9)

heat_exchanger.add_connectors_in(pipe_7)
heat_exchanger.add_connectors_out(pipe_3)

pump_2.add_connectors_in(pipe_3)
pump_2.add_connectors_out(pipe_4)

mixing_chamber.add_connectors_in(pipe_4)
mixing_chamber.add_connectors_in(pipe_9)
mixing_chamber.add_connectors_out(pipe_5)


recicled_rankine_power_cycle = ThermoCycle()
recicled_rankine_power_cycle.add_equipment(pump_1)
recicled_rankine_power_cycle.add_equipment(pump_2)
recicled_rankine_power_cycle.add_equipment(turbine)
recicled_rankine_power_cycle.add_equipment(condenser)
recicled_rankine_power_cycle.add_equipment(heater)
recicled_rankine_power_cycle.add_equipment(heat_exchanger)
recicled_rankine_power_cycle.add_equipment(mixing_chamber)

recicled_rankine_power_cycle.initialize()
recicled_rankine_power_cycle.draw("T7.png")






