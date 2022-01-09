from assemble_video import assemble_video
from reddit_grabber import RedditImageScraper
from text_to_speech import text_to_speech
from youtube_video_helper import upload_file
from dotenv import load_dotenv
from detect_text import detect_text


def main():
    load_dotenv()
    # detect_text()
    # upload_file('test1.mov', 'test 2 aajdsakha',
    #             'typical descrition', ['tag2', 'tag1'], 'public')
    image_paths = RedditImageScraper(limit=5, order="hot").get_images()
    # print(image_paths)
    for path in image_paths:
        text = detect_text(path["file_path"])
        if text != "":
            text_to_speech(text, path["root_path"])

    assemble_video(image_paths)


if __name__ == '__main__':
    main()
