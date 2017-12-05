import csv
import time

def bday_checker(dic,month,day):
    lis=[] #to store multiple bday on same date
    for a in dic:                                                      # To check bday on current date
        if int(a)==month:
            for  x in dic[a]:
                temp=int(x[1][0:2])
                if temp==day:
                    lis.append(x[0])
                    print "Bdaysssss"
    return lis
                
month=time.localtime(time.time())[1]   #current month acc to system
day=time.localtime(time.time())[2]      #current day acc to system
dic={} #To store month wise bdays

file_name='b_days.csv'

with open(file_name) as csvfile:
    readCSV = csv.reader(csvfile, delimiter=',')
    for row in readCSV:
        print(row)
        if dic.has_key(row[1][3:5]):
            dic[row[1][3:5]].append(row)
        else:
            dic[row[1][3:5]]=[row]
            
print bday_checker(dic,month,day)
