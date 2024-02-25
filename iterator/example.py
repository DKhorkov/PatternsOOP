from collections.abc import Iterator
from datetime import datetime
from typing import AnyStr

from employees_collection import EmployeesCollection
from employee import Employee


class Example:

    def __init__(self) -> None:
        self.__employees_collection = EmployeesCollection(
            employees=[
                Employee(
                    name='Maksim',
                    surname='Sorokin',
                    birthday=datetime(year=1990, month=1, day=21),
                    address='Russia, Saint-Petersburg, Moscowsky Prospect 220',
                    email='msorokin@gmail.com',
                    phone='+7-951-246-97-52',
                    job_title='Devops',
                    hire_date=datetime(year=2021, month=7, day=15),
                    salary=80_000,
                    fired=True,
                    dismissal_date=datetime(year=2023, month=12, day=20)
                ),
                Employee(
                    name='Andrey',
                    surname='Boyarsky',
                    birthday=datetime(year=1985, month=10, day=5),
                    address='Russia, Saint-Petersburg, Moscowsky Prospect 15',
                    email='aboyarsky@gmail.com',
                    phone='+7-911-843-27-86',
                    job_title='Senior Software Developer',
                    hire_date=datetime(year=2018, month=6, day=19),
                    salary=250_000,
                ),
                Employee(
                    name='Pavel',
                    surname='Ivanov',
                    birthday=datetime(year=1982, month=9, day=27),
                    address='Russia, Saint-Petersburg, Moscowsky Prospect 198',
                    email='pivanov@gmail.com',
                    phone='+7-921-547-63-48',
                    job_title='Project Manager',
                    hire_date=datetime(year=2017, month=4, day=16),
                    salary=150_000
                ),
                Employee(
                    name='Mark',
                    surname='Zverev',
                    birthday=datetime(year=1996, month=11, day=6),
                    address='Russia, Saint-Petersburg, Moscowsky Prospect 27',
                    email='mzverev@gmail.com',
                    phone='+7-921-358-46-11',
                    job_title='SMM Manager',
                    hire_date=datetime(year=2023, month=1, day=17),
                    salary=65_000,
                    fired=True,
                    dismissal_date=datetime(year=2023, month=10, day=5)
                )
            ]
        )

    def iterate_through_employees(self) -> None:
        print('\nIterating through all employees:\n')
        for employee in self.__employees_collection:
            self.__describe_employee(employee=employee)

    def iterate_through_not_fired_employees(self) -> None:
        print('\nIterating through not fired employees:\n')
        iterator: Iterator = self.__employees_collection.get_not_fired_employees_iterator()
        for employee in iterator:
            self.__describe_employee(employee=employee)

    @staticmethod
    def __describe_employee(employee: Employee) -> None:
        description: AnyStr = '\n'.join([f'{key}: {value}' for key, value in employee.dict().items()])
        print(description, end='\n' * 3)


if __name__ == '__main__':
    example = Example()
    example.iterate_through_employees()
    example.iterate_through_not_fired_employees()
