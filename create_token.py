from __future__ import print_function
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request


def main():
    creds = None
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json',
                ['https://www.googleapis.com/auth/drive.file', ],
            )
            creds = flow.run_console()

        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)

    _ = build('drive', 'v3', credentials=creds) \
        .files().list(pageSize=10, fields="nextPageToken, files(id, name)") \
        .execute()


if __name__ == '__main__':
    main()
