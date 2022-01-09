from assemble_video import assemble_video
from reddit_grabber import RedditImageScraper
from text_to_speech import text_to_speech
from youtube_video_helper import upload_file
from dotenv import load_dotenv
from detect_text import detect_text


def main():
    load_dotenv()
    image_paths = RedditImageScraper(limit=10, order="hot").get_images()
    loading = 0
    for path in image_paths:
        text = detect_text(path["file_path"])
        text = repr(text).replace("\n", ".", -1)
        if text != "":
            text_to_speech(text, path["root_path"])
        loading += 1
        print(f"{int((loading / len(image_paths) * 100))} %")

    gotowe_path = assemble_video(image_paths)

    upload_file(gotowe_path, '[FUNNY] #Shorts',
                'typical smiezne sfilmiki fajne smizenesze descrition', ['zabawa', 'smiechawa', 'super XD'], 'public')


if __name__ == '__main__':
    main()
