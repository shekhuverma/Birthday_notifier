import csv
import requests
import time

from credentials import Id
import twilio_setup
month=time.localtime(time.time())[1]   #current month acc to system
day=time.localtime(time.time())[2]      #current day acc to system
dic={} #To store month wise bdays



CSV_URL = 'https://docs.google.com/spreadsheets/d/'+str(Id)+'/export?format=csv'

with requests.Session() as s:                         #To get the user data from google drive and saving it in a dictionary
    download = s.get(CSV_URL)
    decoded_content = download.content.decode('utf-8')
    cr = csv.reader(decoded_content.splitlines(), delimiter=',')
    my_list = list(cr)
    for row in my_list:
        print row
        if dic.has_key(row[1][3:5]):
            dic[row[1][3:5]].append(row)
        else:
            dic[row[1][3:5]]=[row]

def bday_checker(dic):
    lis=[]                                                                  #to store multiple bday on same date
    for a in dic:                                                       # To check bday on current date
        if int(a)==month:
            for  x in dic[a]:
                temp=int(x[1][0:2])
                if temp==day:
                    lis.append(x[0])
    return lis                                                          #Returns the list of names which have bdays on current data
print bday_checker(dic)
twilio_setup.send_sms(bday_checker(dic))         #To send bday alerts on phone

