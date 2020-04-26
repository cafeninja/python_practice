
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import urllib.request  # instead of urllib2 like in Python 2.7
import json
import sys
import os
 
## delete only if file exists ##
if os.path.exists("message.txt"):
    os.remove("message.txt")

# save output of whole script to file.
orig_stdout = sys.stdout
f = open('message.txt', 'w')
sys.stdout = f

# Tell me the day of the week.
today = date.today()
now = datetime.now() 
# retrieve today's weekday (0=Monday, 6=Sunday)
days = ["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
print ("Today is " + days[today.weekday()] + ".")
print (now.strftime("%d %B, %y")) 

# Tell me how old I am.
print("--------------")
bday = date(1971,7,27)
age = today - bday
# requires the "from dateutil.relativedelta import relativedelta"
difference_in_years = relativedelta(today, bday).years
print("You are " + str(difference_in_years) + " years old today.")


# Tell me the next important date for my calendar (Gmail)


####################

# Get the Euro -> USD exchange rate.
urlData = "http://www.floatrates.com/daily/eur.json"

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # # now we can access the contents of the JSON like any other Python object
    # if "title" in theJSON["metadata"]:
    #     print(theJSON["metadata"]["title"])

    # Get the Euro -> USD exchange rate.
    count = theJSON["usd"]["rate"];
    count = round(count, 3)
    print("--------------")
    print ("Euro to USD Exchange rate is: " + str(count))
    #print ("--------------")


# Open the URL and read the data
webUrl = urllib.request.urlopen(urlData)
# print("result code: " + str(webUrl.getcode()))
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
else:
    print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

####################


####################
# temprature stats
import urllib.request  # instead of urllib2 like in Python 2.7
import json


urlData = "http://api.openweathermap.org/data/2.5/weather?q=Birkirkara&appid=5b34cb173dab8eb89fef4a43a245cfd8"
# http://api.openweathermap.org/data/2.5/weather?q=Birkirkara&appid=5b34cb173dab8eb89fef4a43a245cfd8

# prior urlData = "https://pomber.github.io/covid19/timeseries.json"

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)
    # print(theJSON)
    # datakeys= theJSON.keys()
    # print(datakeys)
    # dict_keys(['coord', 'weather', 'base', 'main', 'visibility', 'wind', 'clouds', 'dt', 'sys', 'timezone', 'id', 'name', 'cod'])
    # mtweather= list(theJSON['weather'])
    # print(mtweather)
    # [{'id': 801, 'main': 'Clouds', 'description': 'few clouds', 'icon': '02d'}]
    # mtmain= list(theJSON['main'])
    # print(mtmain)
    # ['temp', 'feels_like', 'temp_min', 'temp_max', 'pressure', 'humidity']   ...  C = K - 273.15

    high = int(theJSON['main']['temp_max'] - 273.15)
    current = int(theJSON['main']['temp'] - 273.15)
    #print(high)
    #print(type(high))
    print("--------------")
    print(f"The high temprature should be {high} C.")
    print(f"Currently the temp is {current} C. ")
    print(f"With current humidity at {theJSON['main']['humidity']}%.")
    print("--------------")     


# Open the URL and read the data
webUrl = urllib.request.urlopen(urlData)
# print("result code: " + str(webUrl.getcode()))
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
else:
    print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

####################

##############
# Covid stats testing
import urllib.request  # instead of urllib2 like in Python 2.7
import json


urlData = "https://pomber.github.io/covid19/timeseries.json"

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    datakeys= theJSON.keys()
    mtdata= list(theJSON["Malta"])
    # print(mtdata)
    
    print("Covid stats for Malta (last four days)")
    print(f"Date:\t\tConfirmed:\t\tDeaths:\t\tRecoveries:")
    last_for = [-4, -3, -2, -1]
    for i in last_for:
        fmt_data= mtdata[i]
        print(f"{fmt_data['date']}\t\t{fmt_data['confirmed']}\t\t\t\t{fmt_data['deaths']}\t\t{fmt_data['recovered']}")
        


# Open the URL and read the data
webUrl = urllib.request.urlopen(urlData)
# print("result code: " + str(webUrl.getcode()))
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
else:
    print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
#########################

# closes the output of script to file and closes it for the message boddyl
sys.stdout = orig_stdout
f.close() 

# Send email with the message body above:
# reference https://realpython.com/python-send-email/#option-2-setting-up-a-local-smtp-server

import smtplib, ssl
m = open("message.txt", "r")
body = m.read()

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "emmettstewart1@gmail.com"
receiver_email = "emmett@ce3ps.com"
password = "prnzxturkdvipwby"
message = "Subject: Daily Report for " + str(today) + "\n\n" + str(body) + "\n\n"

context = ssl.create_default_context()
with smtplib.SMTP(smtp_server, port) as server:
    server.ehlo()  # Can be omitted
    server.starttls(context=context)
    server.ehlo()  # Can be omitted
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)



