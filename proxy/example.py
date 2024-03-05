from pathlib import Path

from downloader import Downloader
from pictures_downloader import PicturesDownloader
from cached_downloader_proxy import CachedDownloaderProxy


if __name__ == '__main__':
    downloader: Downloader = PicturesDownloader()
    path_to_file: Path = downloader.download('cat')
    print(path_to_file)
    path_to_file: Path = downloader.download('cat')
    print(path_to_file)
    path_to_file: Path = downloader.download('cat')
    print(path_to_file)

    downloader: Downloader = CachedDownloaderProxy(downloader=downloader)
    path_to_file: Path = downloader.download('dog')
    print(path_to_file)
    path_to_file: Path = downloader.download('dog')
    print(path_to_file)
    path_to_file: Path = downloader.download('dog')
    print(path_to_file)
    path_to_file: Path = downloader.download('dog')
    print(path_to_file)

