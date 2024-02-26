import json
import os

from typing import Dict, Any, AnyStr
from pathlib import Path

from person_visitor import PersonVisitor
from employee import Employee
from investor import Investor
from configs import EXPORTED_DATA_FOLDER


class JsonExportVisitor(PersonVisitor):

    def visit_employee(self, employee: Employee) -> None:
        exported_data: Dict[AnyStr, Any] = {
            'name': employee.name,
            'surname': employee.surname,
            'salary': employee.salary
        }

        self.__export(exported_data=exported_data)

    def visit_investor(self, investor: Investor) -> None:
        exported_data: Dict[AnyStr, Any] = {
            'name': investor.name,
            'surname': investor.surname,
            'previous_period_stonks_price': investor.previous_period_stonks_price,
            'current_stonks_price': investor.current_stonks_price
        }

        self.__export(exported_data=exported_data)

    def __export(self, exported_data: Dict[AnyStr, Any]) -> None:
        self.__create_exported_data_folder_if_not_exist()

        filename: Path = Path(EXPORTED_DATA_FOLDER / f'{exported_data.get("name")}_{exported_data.get("surname")}.json')
        with open(file=filename, mode='w') as exported_file:
            json.dump(obj=exported_data, fp=exported_file)

    @staticmethod
    def __create_exported_data_folder_if_not_exist():
        if not os.path.exists(path=EXPORTED_DATA_FOLDER):
            os.makedirs(name=EXPORTED_DATA_FOLDER)
