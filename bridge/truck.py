from time import sleep

from car import Car
from configs import EMPTY_FUEL_THRESHOLD, FuelCoefficients, ITERATION_TIMEOUT_SECONDS


class Truck(Car):

    def ride(self) -> None:
        self._is_riding = True
        while self._is_riding:
            if self._fuel < EMPTY_FUEL_THRESHOLD:
                self._emergency_stop()
                break

            wasted_fuel: float
            ridden_miles: int
            wasted_fuel, ridden_miles = self._implementer.use_fuel_to_ride()
            self._fuel -= FuelCoefficients.large_vehicle_weight.value * wasted_fuel
            self._mileage += ridden_miles

            sleep(ITERATION_TIMEOUT_SECONDS)
