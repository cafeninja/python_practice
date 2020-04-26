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
    
    print("Covid stats for Malta (last for days)")
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
