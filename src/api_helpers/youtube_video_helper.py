import os
from typing import List

from googleapiclient.http import MediaFileUpload

from api_helpers.google_api_auth import Create_Service


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

    media_file = MediaFileUpload(str(filename))

    response_upload = service.videos().insert(
        part='snippet,status',
        body=request_body,
        media_body=media_file
    ).execute()

    print(response_upload, "youtube file uploaded")
