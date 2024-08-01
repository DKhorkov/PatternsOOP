from tabular_method.protocols import Animal
from tabular_method.table import PETS

if __name__ == '__main__':
    print(f"Possible pets: {PETS.keys()}")
    pet_type: str = input("Enter a pet type: ").strip().lower()
    while pet_type not in PETS.keys():
        pet_type = input("Incorrect pet type. Try again! Enter a pet type: ").strip().lower()

    pet_name: str = input("Enter a pet name: ").strip()
    pet: Animal = PETS[pet_type](pet_name)
    assert isinstance(pet, Animal)
    pet.make_voice()
