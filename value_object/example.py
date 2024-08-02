from value_object.figure import Figure
from value_object.square import Square


if __name__ == '__main__':
    first_square: Figure = Square(side=20)
    second_square: Figure = first_square.expand(times=2)
    print(first_square)
    print(second_square)
    assert first_square != second_square
