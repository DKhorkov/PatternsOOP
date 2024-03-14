from typing import AnyStr

from file_writer import FileWriter
from configs import FileExtensions, FileModes, Separators


class TXTWriter(FileWriter):

    def _write_to_file(self, filename: AnyStr) -> None:
        with open(f'{filename}.{FileExtensions.txt.value}', FileModes.write.value) as file:
            file.writelines(self._data)

    def _process_data_hook(self) -> None:
        self._data = [elem + Separators.new_line.value for elem in self._data]
