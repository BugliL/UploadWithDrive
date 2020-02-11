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


def tar_gz_files(fname: str) -> None:
    with tarfile.open(fname, "w:gz") as tar:
        for name in [word]:
            tar.add(name)


def upload_tar_gz_file(name: str) -> dict:
    media = MediaFileUpload(name, mimetype='application/tar+gzip', )
    drive_service = build('drive', 'v3', credentials=get_credentials())
    return drive_service.files().create(
        body={
            'name': name,
            'parents': [secrets.FOLDER_ID],
        },
        media_body=media,
        fields='id',
    ).execute()


if __name__ == '__main__':
    word, file_name = sys.argv[1:]
    time_string = time.strftime("%Y%m%d_%H%M")
    name = file_name + '_' + time_string + '.tar.gz'

    tar_gz_files(name)
    file = upload_tar_gz_file(name)
    print('File ID: %s' % file.get('id'))
