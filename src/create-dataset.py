
import os, sys
from pathlib import Path
from icrawler.builtin import BaiduImageCrawler, GoogleImageCrawler, BingImageCrawler


def start_crawler(path:Path, search_text, num_images):

    crawler = BaiduImageCrawler(
            feeder_threads=2,
            parser_threads=2,
            downloader_threads=4,
            storage={'root_dir': path})

    crawler.crawl(keyword=search_text,
                  min_size=(64, 64),
                  max_num=num_images)


if __name__ == '__main__':
    if len(sys.argv) < 3:
        print(f'usage: python {sys.argv[0]} <searched text> <number of images> ')
        exit(1)

    search_text = sys.argv[1]
    num_images = int(sys.argv[2])
    path = os.path.join(os.getcwd(),'dataset',search_text)
    print(f'downloading {num_images} images for {search_text} into {path}')

    start_crawler(path, search_text, num_images)

