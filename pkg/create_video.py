import re

from dotenv import load_dotenv

from assemble_video import assemble_video
from api_helpers.detect_text import detect_text
from api_helpers.reddit_grabber import RedditImageScraper
from api_helpers.text_to_speech import text_to_speech


def create_video(subreddit: str, image_limit: int, order: str):
    load_dotenv()

    image_paths = RedditImageScraper(subreddit=subreddit,
                                     limit=image_limit, order=order).get_images()

    for path in image_paths:
        text = detect_text(path["image_path"])
        text = text.replace("\n", " ", -1)
        text = re.sub(r'[^A-Za-z0-9 "]+', '', text)
        if text != "":
            text_to_speech(text, path["root_path"])

    assemble_video(image_paths)

    # upload_file(filename=ProjectPaths.OUTPUT_VIDEO,
    #             title='[FUNNY] [gigafunny] [SHOCKING] meme DANK MEGA COMP',
    #             description='Hej kochani dzieki za kino dzisiaj fajnie było co sądzicie o tym i co naley zmienić????',
    #             tags=['Shorts', 'funny', 'memes', "meme"],
    # privacy_status='private')


if __name__ == '__main__':
    create_video("dankmemes", 10, "hot")
