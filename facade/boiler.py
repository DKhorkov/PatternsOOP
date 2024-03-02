from water import Water
from configs import LiquidTemperatures


class Boiler:

    @staticmethod
    def boil_water(water: Water) -> Water:
        water.temperature = LiquidTemperatures.boiling.value
        return water
