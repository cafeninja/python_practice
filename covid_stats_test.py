# Covid stats testing
import urllib.request  # instead of urllib2 like in Python 2.7
import json


urlData = "https://pomber.github.io/covid19/timeseries.json"

def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    # # now we can access the contents of the JSON like any other Python object
    # if "title" in theJSON["metadata"]:
    #     print(theJSON["metadata"]["title"])

    # Get the Euro -> USD exchange rate.
    ## count = theJSON["usd"]["rate"];
    ## count = round(count, 3)
    ## print("--------------")
    ## print ("Euro to USD Exchange rate is: " + str(count))
    ## print ("--------------")

    #Get the date for Malta.
    mtdata= list(theJSON["Malta"])
    # for troubleshooting, show what we have now
    # print(mtdates)
    for i in mtdata:
    	print(f"{i}")


# Open the URL and read the data
webUrl = urllib.request.urlopen(urlData)
# print("result code: " + str(webUrl.getcode()))
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
else:
    print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
