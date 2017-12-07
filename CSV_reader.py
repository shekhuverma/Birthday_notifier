import csv
import time

import pickle

pickle_out = open("dic.pickle","wb")
month=time.localtime(time.time())[1]   #current month acc to system
day=time.localtime(time.time())[2]      #current day acc to system
dic={} #To store month wise bdays

file_name='b_days.csv'

def bday_checker(dic):
    lis=[] #to store multiple bday on same date
    for a in dic:                                                      # To check bday on current date
        if int(a)==month:
            for  x in dic[a]:
                temp=int(x[1][0:2])
                if temp==day:
                    lis.append(x[0])
    return lis
                
def list_data(file_name):
    with open(file_name) as csvfile:
        readCSV = csv.reader(csvfile, delimiter=',')
        for row in readCSV:
            print(row)
            if dic.has_key(row[1][3:5]):
                dic[row[1][3:5]].append(row)
            else:
                dic[row[1][3:5]]=[row]
        pickle.dump(dic, pickle_out)
        pickle_out.close()

