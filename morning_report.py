
from datetime import date
from datetime import time
from datetime import datetime
from datetime import timedelta
from dateutil.relativedelta import relativedelta
import urllib.request  # instead of urllib2 like in Python 2.7
import json

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


# Temp difference today from yesterday.


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
    print ("--------------")


# Open the URL and read the data
webUrl = urllib.request.urlopen(urlData)
# print("result code: " + str(webUrl.getcode()))
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
else:
    print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))

# Show me the line graph of important stat to me.  Maybe try something from Covid-19 source.
# 

