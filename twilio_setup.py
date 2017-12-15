#!/usr/bin/python2.7

# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
from proxied_twilio_http_client import ProxiedTwilioHttpClient    #proxy client for python anywhere

from credentials import account_sid, auth_token,to,from_    #getting the credentials

def sms(message):
##    client = Client(account_sid, auth_token, http_client=ProxiedTwilioHttpClient())
    client = Client(account_sid, auth_token)    #comment when using pythonanywhere and vice versa 
    message = client.messages.create(
        to,from_=from_,
        body=message)


def send_sms(lis):
    for a in lis:
        sms(str(a)+"has bday today")
