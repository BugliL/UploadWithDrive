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
5) python create_file_and_upload.py <ABSOLUTE PATH> <FILENAME>


## Example of secrets.py
```python
FOLDER_ID = 'SPECIAL CODE PROVIDED FROM CREATE_FOLDER.py'
FOLDER_NAME = 'TMP_FOLDER_FOR_UPLOAD'
```