from .decorator import Decorator
from .one_arm_decorator import OneArmDecorator
from .anabolic_decorator import AnabolicDecorator
from .hungover_decorator import HungoverDecorator
from .powerlifter import PowerLifter
from .heavyweight_powerlifter import HeavyWeightPowerLifter


"""
A decorator is a structural design pattern that allows to dynamically add new functionality to objects
by wrapping them in useful “wrappers.”

Simple objects without a lot of internal data are suitable for the decorator.
Otherwise, the “strategy” pattern is better suited.
"""
