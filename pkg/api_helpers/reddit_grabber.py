import os
import re

import praw

from pkg.config.config import REDDIT_CLIENT_ID, REDDIT_CLIENT_SECRET
from pkg.utils.utils import download


class RedditImageScraper:
    def __init__(self, subreddit="memes", limit=10, order="top", nsfw=False):
        self.sub = subreddit
        self.limit = limit
        self.order = order
        self.nsfw = nsfw
        self.path = f'images/{self.sub}/'
        self.reddit = praw.Reddit(client_id=REDDIT_CLIENT_ID,
                                  client_secret=REDDIT_CLIENT_SECRET,
                                  user_agent='reddit image downloader')

    def does_submission_pass_rules(self, submission):
        return not submission.stickied and submission.over_18 == self.nsfw \
               and submission.url.endswith(('jpg', 'jpeg', 'png'))

    def get_images(self):
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
            else:
                submissions = self.reddit.subreddit(self.sub).new(limit=None)

            for submission in submissions:
                if self.does_submission_pass_rules(submission):
                    file_name = re.search(
                        '(?s:.*)\w/(.*)', submission.url).group(1)
                    root_path = self.path + file_name.split('.')[0]
                    image_path = root_path + "/image." + \
                                 file_name.split('.')[1]
                    if not os.path.isfile(image_path):
                        images.append(
                            {'url': submission.url, 'image_path': image_path, 'root_path': root_path})
                        go += 1
                        if go >= self.limit:
                            break

            for image in images:
                os.makedirs(image["root_path"], exist_ok=True)
                download(image["url"], image["image_path"])

        except Exception as e:
            print(e)
        return images
