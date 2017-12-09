# Birthday_notifier
A Python script that reminds you of Birthdays

Getting started:-
Two ways to use this 
1) On you local machine
2) On a cloud (I use pythonanywhere)

On local machine :-

Clone the repository and install the dependencies
Make and twilio account and save the credentials in credentials.py file
Now make a .CSV file on your google drive and add the Birthday's in the following manner -  Name(1st column) Bday(dd-mm)(2nd column)
The advantage the that you can edit your file anytime on google drive and the chanegs will be automatically cloned to the repository.
Now go to google drive api sign up and get you credentials 
Download credentials file and save it as clients_secrets.json in the root folder
Now run list_files.py(only one time step) and find your .CSV file and copy its ID and paste it into data_downloader.py
Now you are done just click master.py and boom you will get the notifications on your mobile.

On cloud computer 
Unfortunately I am not ale to get the .CSV file from google drive into the cloud so you have to manually upload it.
Rest procedure is same but use different fucntion n twilio_setup.py when using python anywhere
