import re

from dotenv import load_dotenv

from pkg.api_helpers.reddit_grabber import RedditImageScraper


def get_images(subreddit: str, image_limit: int, order: str):
    load_dotenv()

    image_paths = RedditImageScraper(subreddit=subreddit,
                                     limit=image_limit, order=order).get_images()

    return image_paths
