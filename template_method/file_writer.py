from abc import ABC, abstractmethod
from typing import List, Any, AnyStr


class FileWriter(ABC):

    def __init__(self) -> None:
        self._data: List[AnyStr] = list()

    def add(self, data: Any) -> None:
        self._data.append(str(data))

    def write(self, filename: AnyStr) -> None:
        """
        Template method, containing algorithm of writing data.

        :param filename: name of file to write data to.
        """

        self._process_data_hook()
        self._write_to_file(filename=filename)

    def _process_data_hook(self) -> None:
        """
        Hook method, that gives subclasses additional points to "wedge" into the template method.
        """

        pass

    @abstractmethod
    def _write_to_file(self,  filename: AnyStr) -> None:
        """
        A method that will be replaced in subclasses due to its different behavior depending on the subclass algorithm.
        """

        raise NotImplementedError
