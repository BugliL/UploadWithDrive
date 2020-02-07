import tarfile
import time
import sys

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
    word = sys.argv[1]
    nome_file = sys.argv[2]
    timestr = time.strftime("%Y%m%d_%H%M")
    print(timestr)

    with tarfile.open(nome_file + '_' + timestr + '.tar.gz', "w:gz") as tar:
        for name in [word]:
            tar.add(name)

    media = MediaFileUpload(nome_file + '_' + timestr + '.tar.gz', mimetype='image/jpeg')
    drive_service = build('drive', 'v3', credentials=get_credentials())
    file = drive_service.files().create(
        body={
            'name': nome_file + '_' + timestr + '.tar.gz',

        },
        media_body=media,
        fields='id',
    ).execute()

    print('File ID: %s' % file.get('id'))
