from pathlib import Path
from typing import AnyStr, Dict

from downloader import Downloader


class CachedDownloaderProxy(Downloader):

    def __init__(self, downloader: Downloader) -> None:
        self.__downloader: Downloader = downloader
        self.__cache: Dict[AnyStr, Path] = dict()

    def download(self, name: AnyStr) -> Path:
        if name in self.__cache:
            print(f'Already have downloaded file for "{name}" query and cached path to it:')
            return self.__cache[name]

        path_to_file: Path = self.__downloader.download(name=name)
        self.__cache[name] = path_to_file
        return path_to_file
