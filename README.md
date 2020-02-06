# Upload to drive
Repository to check and try things with Google Drive Python Api

## Install requirements
```bash
$ pip install -r requirements.txt
$ echo "FOLDER_NAME = 'your_folder_name'" > secrets.py
```

## How to use it
1) python create_token.py
2) Authenticate and allow application
3) python create_folder.py
4) take folder id and do
    ```bash
    $ echo "FOLDER_ID = 'your_folder_id'" >> secrets.py
    ```
5) python upload_file


Next version will be improved to zip folder and contents and take parameters from command line.