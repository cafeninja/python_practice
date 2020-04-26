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
