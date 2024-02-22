from heavyweight_powerlifter import HeavyWeightPowerLifter
from one_arm_decorator import OneArmDecorator
from anabolic_decorator import AnabolicDecorator
from hungover_decorator import HungoverDecorator
from exceptions import WeightClassError


class Example:

    def __init__(self) -> None:
        self.__powerlifter: HeavyWeightPowerLifter = HeavyWeightPowerLifter(weight=115)

    @staticmethod
    def weight_class_violation() -> None:
        try:
            HeavyWeightPowerLifter(weight=90)
        except WeightClassError as e:
            print(e)

    def anabolic_deadlift(self) -> float:
        deadlift_weight = AnabolicDecorator(self.__powerlifter).get_deadlift_weight()
        print(f'The powerlifter under anabolic steroids was able to make a deadlift of {deadlift_weight:.2f}.')
        return deadlift_weight

    def one_armed_deadlift(self) -> float:
        deadlift_weight = OneArmDecorator(self.__powerlifter).get_deadlift_weight()
        print(f'The powerlifter with one arm was able to make a deadlift of {deadlift_weight:.2f}.')
        return deadlift_weight

    def hungover_deadlift(self) -> float:
        deadlift_weight = HungoverDecorator(self.__powerlifter).get_deadlift_weight()
        print(f'The powerlifter with a hangover was able to make a deadlift of {deadlift_weight:.2f}.')
        return deadlift_weight

    def mixed_deadlift(self) -> float:
        deadlift_weight = AnabolicDecorator(
            OneArmDecorator(
                HungoverDecorator(
                    self.__powerlifter
                )
            )
        ).get_deadlift_weight()

        print(
            f'The powerlifter under anabolic steroids with only one arm and hangover was able to '
            f'make a deadlift of {deadlift_weight:.2f}.'
        )
        return deadlift_weight


if __name__ == '__main__':
    example = Example()
    example.weight_class_violation()
    anabolic_deadlift = example.anabolic_deadlift()
    one_armed_deadlift = example.one_armed_deadlift()
    hungover_deadlift = example.hungover_deadlift()
    mixed_deadlift = example.mixed_deadlift()
