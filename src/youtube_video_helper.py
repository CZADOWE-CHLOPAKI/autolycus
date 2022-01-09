import datetime
from Google import Create_Service
from googleapiclient.http import MediaFileUpload


CLIENT_SECRET_FILE = 'client_secrets.json'
API_NAME = 'youtube'
API_VERSION = 'v3'
SCOPES = ['https://www.googleapis.com/auth/youtube.upload']


def upload_file(filename: str, title: str, description: str, tags: list[str], privacy_status: str):
    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    # its in the past so it uploads as soon as posible
    upload_date_time = datetime.datetime(
        2020, 12, 25, 12, 30, 0).isoformat() + '.000Z'

    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': title,
            'description': description,
            'tags': tags
        },
        'status': {
            'privacyStatus': privacy_status,
            'publishAt': upload_date_time,
            'selfDeclaredMadeForKids': False,
        },
        'notifySubscribers': False
    }

    mediaFile = MediaFileUpload(filename)

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=mediaFile
    ).execute()
