import configparser
import os
import re
from typing import List

import praw

from src.utils import download


class RedditImageScraper:
    def __init__(self, subreddit="dankmemes", limit=10, order="top", nsfw=False):
        config = configparser.ConfigParser()
        config.read('config.ini')
        self.sub = subreddit
        self.limit = limit
        self.order = order
        self.nsfw = nsfw
        self.path = f'images/{self.sub}/'
        self.reddit = praw.Reddit(client_id=config['REDDIT']['client_id'],
                                  client_secret=config['REDDIT']['client_secret'],
                                  user_agent='reddit image downloader')

    def get_images(self) -> List[str]:
        """
        Gets images from subreddit.
        Returns array of downloaded filenames.
        """
        images = []
        try:
            go = 0
            if self.order == 'hot':
                submissions = self.reddit.subreddit(self.sub).hot(limit=None)
            elif self.order == 'top':
                submissions = self.reddit.subreddit(self.sub).top(limit=None)
            elif self.order == 'new':
                submissions = self.reddit.subreddit(self.sub).new(limit=None)

            for submission in submissions:
                if not submission.stickied and submission.over_18 == self.nsfw \
                        and submission.url.endswith(('jpg', 'jpeg', 'png')):
                    fname = self.path + re.search('(?s:.*)\w/(.*)', submission.url).group(1)
                    if not os.path.isfile(fname):
                        images.append({'url': submission.url, 'file_name': fname})
                        go += 1
                        if go >= self.limit:
                            break

            if not os.path.exists(self.path):
                os.makedirs(self.path)
            for image in images:
                download(image["url"], image["file_name"])
        except Exception as e:
            print(e)
        return [img['file_name'] for img in images]
