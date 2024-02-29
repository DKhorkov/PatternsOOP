from car_builder import CarBuilder


class Director:
    """
    A separate director class is not strictly required. Client can also call builder methods directly.
    However, the director is useful if there are multiple ways to design products that differ in the order and
    presence of design steps. In this case, all this logic can be combined in one class.

    This class structure will completely hide the process of constructing objects from the client code.
    The client will only have to link the desired builder to the director, and then receive the finished
    result from the builder.
    """

    @staticmethod
    def build_sport_car(builder: CarBuilder) -> None:
        builder.reset()
        builder.set_engine('V12')
        builder.set_transmission('automatic')
        builder.set_breaks('carbon ceramic')
        builder.set_seats(2)
        builder.set_spoiler()

    @staticmethod
    def build_truck(builder: CarBuilder) -> None:
        builder.reset()
        builder.set_engine('V8')
        builder.set_seats(8)
        builder.set_wheels(6)
        builder.set_conditioner()
        builder.set_gps()
