from pathlib import Path

from dotenv import load_dotenv

from assemble_video import assemble_video
from detect_text import detect_text
from reddit_grabber import RedditImageScraper
from config import ProjectPaths
from src.utils import create_path_if_not_exists
from text_to_speech import text_to_speech
from youtube_video_helper import upload_file


def main():
    load_dotenv()
    image_paths = RedditImageScraper(limit=5, order="hot").get_images()
    loading = 0
    for path in image_paths:
        text = detect_text(path["file_path"])
        text = text.replace("\n", "", -1)
        if text != "":
            text_to_speech(text, path["root_path"])
        loading += 1
        print(f"{int((loading / len(image_paths) * 100))} %")

    assemble_video(image_paths)

    # upload_file(filename=ProjectPaths.OUTPUT_VIDEO,
    #             title='[FUNNY] #Shorts 10',
    #             description='Super funny memes compilation',
    #             tags=['Shorts', 'funny', 'memes', "meme"],
    #             privacy_status='public')


if __name__ == '__main__':
    main()
