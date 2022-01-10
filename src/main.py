from dotenv import load_dotenv

from assemble_video import assemble_video
from detect_text import detect_text
from reddit_grabber import RedditImageScraper
from text_to_speech import text_to_speech
from youtube_video_helper import upload_file


def main():
    load_dotenv()
    image_paths = RedditImageScraper(limit=10, order="hot").get_images()
    loading = 0
    for path in image_paths:
        text = detect_text(path["file_path"])
        text = text.replace("\n", "", -1)
        if text != "":
            text_to_speech(text, path["root_path"])
        loading += 1
        print(f"{int((loading / len(image_paths) * 100))} %")

    gotowe_path = assemble_video(image_paths)

    upload_file(filename=gotowe_path,
                title='[FUNNY] #Shorts',
                description='typical smiezne sfilmiki fajne smizenesze descrition',
                tags=['zabawa', 'smiechawa', 'super XD'],
                privacy_status='public')


if __name__ == '__main__':
    main()
