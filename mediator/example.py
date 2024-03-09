from time import sleep

from car import Car
from chainsaw import Chainsaw
from car_mediator import CarMediator
from chainsaw_mediator import ChainsawMediator


if __name__ == '__main__':
    print('\nWorking with chainsaw\n')
    chainsaw_mediator: ChainsawMediator = ChainsawMediator()
    chainsaw: Chainsaw = chainsaw_mediator.chainsaw
    chainsaw.start()
    sleep(2)
    chainsaw.stop()

    print('\nWorking with car\n')
    car_mediator: CarMediator = CarMediator()
    car: Car = car_mediator.car
    car.start()
    sleep(2)
    car.stop()
