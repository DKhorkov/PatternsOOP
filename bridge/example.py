from threading import Thread
from time import sleep

from jeep import Jeep
from truck import Truck
from diesel_car_implementer import DieselCarImplementer
from gasoline_car_implementer import GasolineCarImplementer
from configs import ITERATION_TIMEOUT_SECONDS


class Example:

    def __init__(self) -> None:
        self.__full_fuel: float = 100.00

    def __create_diesel_cars(self) -> None:
        self.__diesel_jeep: Jeep = Jeep(fuel=self.__full_fuel, implementer=DieselCarImplementer())
        self.__diesel_truck: Truck = Truck(fuel=self.__full_fuel, implementer=DieselCarImplementer())

    def __create_gasoline_cars(self) -> None:
        self.__gasoline_jeep: Jeep = Jeep(fuel=self.__full_fuel, implementer=GasolineCarImplementer())
        self.__gasoline_truck: Truck = Truck(fuel=self.__full_fuel, implementer=GasolineCarImplementer())

    def compare_diesel_cars(self) -> None:
        self.__create_diesel_cars()
        Thread(target=self.__diesel_jeep.ride).start()
        Thread(target=self.__diesel_truck.ride).start()
        sleep(ITERATION_TIMEOUT_SECONDS)

        self.__diesel_jeep.stop()
        print(
            f'Diesel jeep consumed {(self.__full_fuel - self.__diesel_jeep.fuel):.2f} liters of fuel '
            f'to run {self.__diesel_jeep.mileage} kilometers!'
        )

        self.__diesel_truck.stop()
        print(
            f'Diesel truck consumed {(self.__full_fuel - self.__diesel_truck.fuel):.2f} liters of fuel '
            f'to run {self.__diesel_truck.mileage} kilometers!'
        )

    def compare_gasoline_cars(self) -> None:
        self.__create_gasoline_cars()
        Thread(target=self.__gasoline_jeep.ride).start()
        Thread(target=self.__gasoline_truck.ride).start()
        sleep(ITERATION_TIMEOUT_SECONDS)

        self.__gasoline_jeep.stop()
        print(
            f'Gasoline jeep consumed {(self.__full_fuel - self.__gasoline_jeep.fuel):.2f} liters of fuel '
            f'to run {self.__gasoline_jeep.mileage} kilometers!'
        )

        self.__gasoline_truck.stop()
        print(
            f'Gasoline truck consumed {(self.__full_fuel - self.__gasoline_truck.fuel):.2f} liters of fuel '
            f'to run {self.__gasoline_truck.mileage} kilometers!'
        )

    def raise_emergency_stop(self) -> None:
        self.__create_diesel_cars()
        self.__diesel_truck.ride()


if __name__ == '__main__':
    example = Example()
    example.compare_gasoline_cars()
    example.compare_diesel_cars()
    example.raise_emergency_stop()
