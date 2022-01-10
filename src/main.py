import re

from dotenv import load_dotenv

from assemble_video import assemble_video
from api_helpers.detect_text import detect_text
from api_helpers.reddit_grabber import RedditImageScraper
from api_helpers.text_to_speech import text_to_speech
from utils import print_progress_bar


def main():
    load_dotenv()

    image_limit = 7
    image_paths = RedditImageScraper(
        limit=image_limit, order="hot").get_images()

    loading = 0
    loading_bar_prefix, loading_bar_suffix = 'vision & speech', 'done'
    print_progress_bar(loading, image_limit,
                       loading_bar_prefix, loading_bar_suffix)
    for path in image_paths:
        text = detect_text(path["file_path"])
        text = text.replace("\n", " ", -1)
        # print(f"before: '{text}'")
        text = re.sub(r'[^A-Za-z0-9 "]+', '', text)
        # print(f"after: '{text}'")
        if text != "":
            text_to_speech(text, path["root_path"])

        loading += 1
        print_progress_bar(loading, image_limit,
                           loading_bar_prefix, loading_bar_suffix)

    assemble_video(image_paths)

    # upload_file(filename=ProjectPaths.OUTPUT_VIDEO,
    #             title='[FUNNY] #Shorts 10',
    #             description='Super funny memes compilation',
    #             tags=['Shorts', 'funny', 'memes', "meme"],
    #             privacy_status='public')


if __name__ == '__main__':
    main()
