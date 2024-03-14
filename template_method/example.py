from typing import List, AnyStr

from txt_writer import TXTWriter
from csv_writer import CSVWriter


if __name__ == '__main__':
    filename: AnyStr = 'example'
    data_to_write: List[AnyStr] = [
        'Let',
        'writers',
        'show',
        'their',
        'work'
    ]

    csv_writer: CSVWriter = CSVWriter()
    txt_writer: TXTWriter = TXTWriter()

    for data in data_to_write:
        csv_writer.add(data=data)
        txt_writer.add(data=data)

    csv_writer.write(filename=filename)
    txt_writer.write(filename=filename)
