import time
import CSV_reader,twilio_setup
import pickle
CSV_reader.list_data("b_days.csv")
pickle_in = open("dic.pickle","rb")
dic = pickle.load(pickle_in)
bday=CSV_reader.bday_checker(dic)
for a in bday:
    twilio_setup.send_sms("Today is "+str(a)+"'s Bday")
