from googleapiclient.discovery import build

from secrets import FOLDER_NAME
from upload_file import get_credentials

if __name__ == '__main__':
    file_metadata = {
        'name': FOLDER_NAME,
        'mimeType': 'application/vnd.google-apps.folder'
    }
    drive_service = build('drive', 'v3', credentials=get_credentials())
    file = drive_service.files().create(body=file_metadata, fields='id').execute()
    print('Folder ID: %s' % file.get('id'))
