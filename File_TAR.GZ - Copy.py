import tarfile
import time
import sys

import os
import pickle
import secrets

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload


def get_credentials():
    global creds
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            return pickle.load(token)


if __name__ == '__main__':

    word = sys.argv[1]
    nome_file = sys.argv[2]
    timestr = time.strftime("%Y%m%d_%H%M")
    print(timestr)

    with tarfile.open(nome_file + timestr + '.tar.gz', "w:gz") as tar:
        for name in [word]:
            tar.add(name)

    media = MediaFileUpload(nome_file + timestr + '.tar.gz', mimetype='image/jpeg')
    drive_service = build('drive', 'v3', credentials=get_credentials())
    file = drive_service.files().create(
        body={
            'name': 'minions.jpg',
            'parents': [secrets.FOLDER_ID],
        },
        media_body=media,
        fields='id',
    ).execute()

    print('File ID: %s' % file.get('id'))
