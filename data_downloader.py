from pydrive.drive import GoogleDrive
from pydrive.auth import GoogleAuth

gauth = GoogleAuth()
drive = GoogleDrive(gauth)
#b_days.csv, mimeType: application/vnd.google-apps.spreadsheet
#id = 1kUpKVZXbzC7IF2ROrYICreAg-gku31cnEavMJ_suOWE
file6 = drive.CreateFile({'id': '1kUpKVZXbzC7IF2ROrYICreAg-gku31cnEavMJ_suOWE'})
file6.GetContentFile(file6['title'],mimetype='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')


##file_list = drive.ListFile({'q': "'root' in parents and trashed=false"}).GetList()
##for file1 in file_list:
##  print('title: %s, id: %s' % (file1['title'], file1['id']))
