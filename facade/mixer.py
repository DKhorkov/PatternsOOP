from milk import Milk

from configs import MilkConditions


class Mixer:

    @staticmethod
    def froth_milk(milk: Milk) -> Milk:
        milk.condition = MilkConditions.frothed.value
        return milk
