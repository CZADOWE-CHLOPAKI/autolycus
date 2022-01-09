import argparse
import concurrent.futures
import configparser
import os
import re

import praw

from src.utils import download


# code definitely not stolen from the depths of the internet
class RedditImageScraper:
    def __init__(self, subreddit, limit, order, nsfw=False):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.sub = subreddit
        self.limit = limit
        self.order = order
        self.nsfw = nsfw
        self.path = f'images/{self.sub}/'
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                                  client_secret=config['REDDIT']['client_secret'],
                                  user_agent='Multithreaded Reddit Image Downloader v2.0 (by u/impshum)')

    def start(self):
        images = []
        try:
            go = 0
            if self.order == 'hot':
                submissions = self.reddit.subreddit(self.sub).hot(limit=None)
            elif self.order == 'top':
                submissions = self.reddit.subreddit(self.sub).top(limit=None)
            else:  # sort by new
                submissions = self.reddit.subreddit(self.sub).new(limit=None)

            for submission in submissions:
                if not submission.stickied and submission.over_18 == self.nsfw \
                        and submission.url.endswith(('jpg', 'jpeg', 'png')):
                    file_name = self.path + re.search('(?s:.*)\w/(.*)', submission.url).group(1)
                    if not os.path.isfile(file_name):
                        images.append({'url': submission.url, 'file_name': file_name})
                        go += 1
                        if go >= self.limit:
                            break
            if len(images):
                if not os.path.exists(self.path):
                    os.makedirs(self.path)
                with concurrent.futures.ThreadPoolExecutor() as ptolemy:
                    ptolemy.map(download, images)
        except Exception as e:
            print(e)


def main():
    parser = argparse.ArgumentParser(description='Multithreaded Reddit Image Downloader v2.0 (by u/impshum)')
    required_args = parser.add_argument_group('required arguments')
    required_args.add_argument('-s', type=str, help="subreddit", required=True)
    required_args.add_argument('-i', type=int, help="number of images", required=True)
    required_args.add_argument('-o', type=str, help="order (new/top/hot)", required=True)

    args = parser.parse_args()

    scraper = RedditImageScraper(args.s, args.i, args.o)
    scraper.start()


if __name__ == '__main__':
    main()
