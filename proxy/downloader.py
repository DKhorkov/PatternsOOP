from abc import ABC, abstractmethod
from typing import AnyStr
from pathlib import Path


class Downloader(ABC):

    @abstractmethod
    def download(self, name: AnyStr) -> Path:
        raise NotImplementedError
