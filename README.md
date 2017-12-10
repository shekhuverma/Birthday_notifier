# Birthday_notifier
It scans the Bdays.CSV(which you need to create) file from your google drive and use it as base. You can this .CSV file anytime and program will automatically update itself everytime it will be run. It sends the reminder SMS on your phone  and you can run this setup on any cloud platform (I used Pythonanywhere)

## Getting Started

Clone this repository and follow the instructions.
### Prerequisites

* [Google Drive API credentials](https://developers.google.com/drive/)
* [Twilio API Credentials](https://www.twilio.com/)

### Installing

Install the requirements.txt using PIP

One by one like this
```
pip install pydrive
```

OR

```
pip install -r requirements.txt

```

## Deployment

### Two ways to use this 
1) On you local machine
2) On a cloud (I use pythonanywhere)

#### On your local machine
* Make and twilio account and save the credentials in the respectives fields in credentials.py file
* [Setup PyDrive](https://googledrive.github.io/PyDrive/docs/build/html/quickstart.html) go thorough this and follow each step carefully.
* Download credentials file and save it as clients_secrets.json in the root folder
* Now make a .CSV file in your google drive and add the Birthday's in the following manner -  Name(1st column) Bday(dd-mm)(2nd column)
* The advantage is that you can edit your file anytime on google drive and the changes will be automatically cloned to the repository.
* Now run list_files.py(only one time step) and find your .CSV file and copy its ID and paste it into data_downloader.py
* Now you are done just click master.py and boom you will get the notifications on your mobile.
* You can setup this entire thing on a cloud so that it can run forever

#### On cloud computer 
*Unfortunately I am not ale to get the .CSV file from google drive into the cloud so you have to manually upload it to your cloud system rest procedure is same*
**Quicknote** :- If you are using pythonanywhere then just upload all the files and add Master_PA.py to pythonanywhere/tasks and schdule it. This will make it run every 24 hours and you'll get a  notifications on your phone via SMS 

## Built With

* [Pydrive](https://github.com/googledrive/PyDrive) - To Get the files from Google drive
* [Twilio](https://github.com/twilio/twilio-python) - Sending SMS notifications

## Contributing
If you think your can make this a better better then please go ahead and submit PULL requests
