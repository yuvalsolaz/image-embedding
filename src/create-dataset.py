
import os, sys, shutil
from pathlib import Path
import hashlib, magic
import icrawler
from icrawler.builtin import GoogleImageCrawler, BingImageCrawler


def start_crawler(Crawler_class:icrawler, path:Path, search_text:str, num_images:int, file_idx_offset=0):
    """Kicks off a icarwler download."""
    crawler = Crawler_class(
            feeder_threads=2,
            parser_threads=2,
            downloader_threads=8,
            storage={'root_dir': path})
    crawler.crawl(keyword=search_text, max_num=num_images, file_idx_offset=0)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'usage: python {sys.argv[0]} <searched text> <number of images> ')
        exit(1)

    search_text = sys.argv[1]
    num_images = int(sys.argv[2])
    path = os.path.join(os.getcwd(),'dataset')
    print(f'downloading {num_images} images for {search_text} into {path}')

    start_crawler(BingImageCrawler, path, search_text, num_images, file_idx_offset='auto')

