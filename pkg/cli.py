import re

from dotenv import load_dotenv

from pkg.api_helpers.detect_text import detect_text
from pkg.api_helpers.reddit_grabber import RedditImageScraper
from pkg.api_helpers.text_to_speech import text_to_speech
from pkg.utils.VideoSound import VideoSound
from pkg.utils.utils import print_progress_bar


def main():
    load_dotenv()

    image_limit = 7
    image_paths = RedditImageScraper(subreddit='me_irl',
                                     limit=image_limit, order="hot").get_images()

    loading = 0
    loading_bar_prefix, loading_bar_suffix = 'vision & speech', 'done'
    print_progress_bar(loading, image_limit,
                       loading_bar_prefix, loading_bar_suffix)
    for path in image_paths:
        text = detect_text(path["image_path"])
        text = text.replace("\n", " ", -1)
        # print(f"before: '{text}'")
        text = re.sub(r'[^A-Za-z0-9 "]+', '', text)
        # print(f"after: '{text}'")
        if text != "":
            text_to_speech(text, path["root_path"])

        loading += 1
        print_progress_bar(loading, image_limit,
                           loading_bar_prefix, loading_bar_suffix)

    video = VideoSound(image_paths)
    video.create_mp4()
    video.convert_mp4_to_webm()

    # upload_file(filename=ProjectPaths.OUTPUT_VIDEO,
    #             title='[FUNNY] [gigafunny] [SHOCKING] meme DANK MEGA COMP',
    #             description='Hej kochani dzieki za kino dzisiaj fajnie było co sądzicie o tym i co naley zmienić????',
    #             tags=['Shorts', 'funny', 'memes', "meme"],
    # privacy_status='private')


if __name__ == '__main__':
    main()
