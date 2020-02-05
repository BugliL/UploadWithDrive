import os
import pickle

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def get_credentials():
    global creds
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            return pickle.load(token)


if __name__ == '__main__':
    media = MediaFileUpload('img/minions.jpg', mimetype='image/jpeg')
    drive_service = build('drive', 'v3', credentials=get_credentials())
    file = drive_service.files().create(
        body={'name': 'minions.jpg'},
        media_body=media,
        fields='id'
    ).execute()

    print('File ID: %s' % file.get('id'))
