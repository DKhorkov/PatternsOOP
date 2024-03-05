from typing import AnyStr
from icrawler.builtin import GoogleImageCrawler
from pathlib import Path

from downloader import Downloader
from configs import PICTURES_DIR, LOG_LEVEL


class PicturesDownloader(Downloader):

    def download(self, name: AnyStr) -> Path:
        path_to_pictures: Path = PICTURES_DIR / name
        crawler: GoogleImageCrawler = GoogleImageCrawler(
            storage={'root_dir': path_to_pictures},
            log_level=LOG_LEVEL
        )
        crawler.crawl(keyword=name, max_num=1)
        return path_to_pictures
