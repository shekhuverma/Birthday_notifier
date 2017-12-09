from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

ID='Enter ID HERE'

gauth = GoogleAuth()
drive = GoogleDrive(gauth)

#b_days.csv, mimeType: application/vnd.google-apps.spreadsheet
#id = 1kUpKVZXbzC7IF2ROrYICreAg-gku31cnEavMJ_suOWE

def call():
    file_ = drive.CreateFile({'id': ID})
    file_.GetContentFile(file_['title'],mimetype='text/csv')
call()
#mimetype='text/csv'
