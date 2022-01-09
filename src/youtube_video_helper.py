import datetime

from typing import List

from Google import Create_Service
from googleapiclient.http import MediaFileUpload
import os


def upload_file(filename: str, title: str, description: str, tags: List[str], privacy_status: str):
    CLIENT_SECRET_FILE = os.getenv('GOOGLE_CLIENT_SECRETS')
    API_NAME = 'youtube'
    API_VERSION = 'v3'
    SCOPES = ['https://www.googleapis.com/auth/youtube.upload']

    service = Create_Service(CLIENT_SECRET_FILE, API_NAME, API_VERSION, SCOPES)

    request_body = {
        'snippet': {
            'categoryI': 19,
            'title': title,
            'description': description,
            'tags': tags
        },
        'status': {
            'privacyStatus': privacy_status,
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
