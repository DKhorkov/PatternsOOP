from detail import Detail
from composite import Composite


if __name__ == '__main__':
    processor = Detail(price=500)
    motherboard = Detail(price=300)
    cooler = Detail(price=50)
    power_unit = Detail(price=100)
    hard_disk_driver = Detail(price=70)
    video_card = Detail(price=800)
    random_access_memory_one = Detail(price=250)
    random_access_memory_two = Detail(price=250)
    case = Detail(price=75)

    personal_computer = Composite()
    if personal_computer.is_composite():
        personal_computer.add(processor)
        personal_computer.add(motherboard)
        personal_computer.add(cooler)
        personal_computer.add(power_unit)
        personal_computer.add(hard_disk_driver)
        personal_computer.add(video_card)
        personal_computer.add(random_access_memory_one)
        personal_computer.add(random_access_memory_two)
        personal_computer.add(case)

    price = personal_computer.price()
    print(f'Price of PC with two RAM is {price}$...')

    # Suppose, user has no money for 2 RAM:
    personal_computer.remove(random_access_memory_one)
    price = personal_computer.price()
    print(f'Price of PC with one RAM is {price}$...')
