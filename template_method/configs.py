from enum import Enum
from typing import AnyStr


class FileExtensions(Enum):
    txt: AnyStr = 'txt'
    csv: AnyStr = 'csv'


class FileModes(Enum):
    read: AnyStr = 'r'
    write: AnyStr = 'w'
    append: AnyStr = 'a'


class Separators(Enum):
    csv: AnyStr = ','
    new_line: AnyStr = '\n'
