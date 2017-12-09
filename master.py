import time
import CSV_reader,twilio_setup,data_downloader
import pickle
data_downloader.call()
CSV_reader.list_data("b_days.csv")
pickle_in = open("dic.pickle","rb")
dic = pickle.load(pickle_in)
bday=CSV_reader.bday_checker(dic)
for a in bday:
    print "Today is "+str(a)+"'s Bday"
    twilio_setup.send_sms("Today is "+str(a)+"'s Bday")
