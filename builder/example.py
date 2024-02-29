from director import Director
from car import Car
from car_builder import CarBuilder


class Example:

    def __init__(self) -> None:
        self.__director = Director()
        self.__car_builder = CarBuilder()

    def build_sport_car(self) -> Car:
        self.__director.build_sport_car(self.__car_builder)
        sport_car: Car = self.__car_builder.car
        print(f'\nSport car is {str(sport_car)}', end='\n\n')
        return sport_car

    def build_truck(self) -> Car:
        self.__director.build_truck(self.__car_builder)
        truck: Car = self.__car_builder.car
        print(f'\nTruck is {str(truck)}', end='\n\n')
        return truck

    def build_luxury_car_without_director(self) -> Car:
        self.__car_builder.reset()
        luxury_car: Car = self.__car_builder.set_engine(
            'V6'
        ).set_seats(
            5
        ).set_transmission(
            'automatic'
        ).set_gps().set_conditioner().set_hatch().car
        print(f'\nLuxury car is {str(luxury_car)}', end='\n\n')
        return luxury_car


if __name__ == '__main__':
    example = Example()
    example.build_sport_car()
    example.build_truck()
    example.build_luxury_car_without_director()
