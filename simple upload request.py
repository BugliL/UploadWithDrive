import os
import pickle

from googleapiclient.discovery import build
from googleapiclient.http import MediaFileUpload

if os.path.exists('token.pickle'):
    with open('token.pickle', 'rb') as token:
        creds = pickle.load(token)

drive_service = build('drive', 'v3', credentials=creds)

file_metadata = {'name': 'minions.jpg'}
media = MediaFileUpload('img/minions.jpg', mimetype='image/jpeg')
file = drive_service.files().create(body=file_metadata, media_body=media, fields='id').execute()
print('File ID: %s' % file.get('id'))
