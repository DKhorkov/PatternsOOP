from typing import Self, AnyStr

from car import Car


class CarBuilder:
    """
    Builder returns itself in each set_ method for cascade creation option.

    Example:
        builder = CarBuilder()
        builder.set_wheels(4).set_engine('V12')
    """

    def __init__(self):
        self._car: Car = Car()

    def reset(self) -> None:
        self.__init__()

    @property
    def car(self) -> Car:
        """
        Returns created Car. After creating a car, it should not be finalized, so reset Builders car parameter.

        :return: Created Car.
        """

        car: Car = self._car
        self.reset()
        return car

    def set_wheels(self, wheels: int) -> Self:
        self._car.wheels = wheels
        return self

    def set_engine(self, engine: AnyStr) -> Self:
        self._car.engine = engine
        return self

    def set_seats(self, seats: int) -> Self:
        self._car.seats = seats
        return self

    def set_transmission(self, transmission: AnyStr) -> Self:
        self._car.transmission = transmission
        return self

    def set_breaks(self, breaks: AnyStr) -> Self:
        self._car.breaks = breaks
        return self

    def set_gps(self) -> Self:
        self._car.gps = True
        return self

    def set_conditioner(self) -> Self:
        self._car.gps = True
        return self

    def set_hatch(self) -> Self:
        self._car.gps = True
        return self

    def set_spoiler(self) -> Self:
        self._car.gps = True
        return self
