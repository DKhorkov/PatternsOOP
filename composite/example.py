from detail import Detail
from composite import Composite


class Example:

    def __init__(self):
        self.__processor = Detail(price=500)
        self.__motherboard = Detail(price=300)
        self.__cooler = Detail(price=50)
        self.__power_unit = Detail(price=100)
        self.__hard_disk_driver = Detail(price=70)
        self.__video_card = Detail(price=800)
        self.__random_access_memory = Detail(price=250)
        self.__case = Detail(price=75)

    def build_user_pc(self) -> Composite:
        personal_computer: Composite = self.__build_pc()
        print(f'Price of PC with one RAM is {personal_computer.price():.2f}$...')

        # Suppose, user wants PC with two RAM:
        personal_computer.add(self.__random_access_memory)
        print(f'Price of PC with two RAM is {personal_computer.price():.2f}$...')

        # Suppose, user has no money for PC with 2 RAM:
        personal_computer.remove(self.__random_access_memory)
        print(
            f'You have not money for PC with two RAM? '
            f'Price of PC with one RAM is {personal_computer.price():.2f}$...'
        )

        return personal_computer

    def __build_pc(self) -> Composite:
        personal_computer: Composite = Composite()
        if personal_computer.is_composite():
            personal_computer.add(self.__processor)
            personal_computer.add(self.__motherboard)
            personal_computer.add(self.__cooler)
            personal_computer.add(self.__power_unit)
            personal_computer.add(self.__hard_disk_driver)
            personal_computer.add(self.__video_card)
            personal_computer.add(self.__random_access_memory)
            personal_computer.add(self.__case)

        return personal_computer

    def build_server_room(self, number_of_pc: int) -> Composite:
        server_room = Composite()
        for i in range(number_of_pc):
            personal_computer: Composite = self.__build_pc()
            server_room.add(personal_computer)

        print(f'Price of server-room with {number_of_pc} PC is {server_room.price():.2f}$...')
        return server_room


if __name__ == '__main__':
    example = Example()
    user_pc = example.build_user_pc()
    server_room = example.build_server_room(number_of_pc=5)
