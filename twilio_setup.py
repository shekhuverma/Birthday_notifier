#!/usr/bin/python2.7

# Download the twilio-python library from twilio.com/docs/libraries/python
from twilio.rest import Client
from proxied_twilio_http_client import ProxiedTwilioHttpClient    #proxy client for python anywhere

from credentials import account_sid, auth_token,to,from_    #getting the credentials

def send_sms(message):
##    client = Client(account_sid, auth_token, http_client=ProxiedTwilioHttpClient())
    client = Client(account_sid, auth_token)    #comment when using pythonanywhere and vice versa 
    message = client.messages.create(
        to,from_=from_,
        body=message)
send_sms("Sent from pc")
