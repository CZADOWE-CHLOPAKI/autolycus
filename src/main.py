from src.reddit_grabber import RedditImageScraper
from youtube_video_helper import upload_file
from dotenv import load_dotenv
from detect_text import detect_text


def main():
    load_dotenv()
    # detect_text()
    # upload_file('test1.mov', 'test 2 aajdsakha',
    #             'typical descrition', ['tag2', 'tag1'], 'public')
    paths = RedditImageScraper(limit=1).get_images()
    for path in paths:
        print(path)
        detect_text(path)


if __name__ == '__main__':
    main()
