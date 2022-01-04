import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def __init__(self, access_token):
        self.access_token =  access_token
    def upload_file(self, file_from, file_to):

        dbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:
                local_path = os.path.join(root, filename)
                relative_path = os.path.relpath(local_path, file_from)
                dropbox_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dbx.files_upload(f.read(), dropbox_path, mode=WriteMode('overwrite'))

def main():
    access_token = 'nyAVxMK6ipkAAAAAAAAAAeGUJLUxC6QKnUpJQRf39gtfsZD5rfZ9B6GYEL4H2bcY'
    transferData = TransferData(access_token)

    file_from = input("Enter the file path to transfer: ")
    file_to = input("Enter the path to upload the file: ") # Enter /RitikClass101/folder_name/file_name

    transferData.upload_file(file_from, file_to)
    print('File has been transferred.')

main()