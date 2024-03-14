from typing import AnyStr, List

from file_writer import FileWriter
from configs import FileExtensions, FileModes, Separators


class CSVWriter(FileWriter):

    def _write_to_file(self, filename: AnyStr) -> None:
        with open(f'{filename}.{FileExtensions.csv.value}', FileModes.write.value) as file:
            file.writelines(self._data)

    def _process_data_hook(self) -> None:
        processed_data: List[AnyStr] = list()
        for elem in self._data:
            processed_data.append(
                Separators.csv.value.join(
                    [char for char in elem]
                ) + Separators.new_line.value
            )

        self._data = processed_data
