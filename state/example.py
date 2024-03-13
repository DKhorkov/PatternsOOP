from meat import Meat
from raw import Raw


if __name__ == '__main__':
    first_piece: Meat = Meat(Raw)
    second_piece: Meat = Meat(Raw)
    third_piece: Meat = Meat(Raw)

    first_piece.eat()

    second_piece.cook()
    second_piece.eat()
    second_piece.cook()
    second_piece.eat()

    third_piece.cook()
    third_piece.cook()
    third_piece.eat()
