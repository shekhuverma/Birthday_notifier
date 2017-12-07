from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

#b_days.csv, mimeType: application/vnd.google-apps.spreadsheet
#id = 1kUpKVZXbzC7IF2ROrYICreAg-gku31cnEavMJ_suOWE

def call():
    file_ = drive.CreateFile({'id': '1kUpKVZXbzC7IF2ROrYICreAg-gku31cnEavMJ_suOWE'})
    file_.GetContentFile(file_['title'],mimetype='text/csv')

#mimetype='text/csv'
import time

interval=20    #In minutes
while True:
    call()
    time.sleep(1*60)
