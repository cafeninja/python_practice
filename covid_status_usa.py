# Covid stats testing
import urllib.request  # instead of urllib2 like in Python 2.7
import json

urlData = "https://pomber.github.io/covid19/timeseries.json"
country = "US"
# county names = Malta, Italy, US, United Kingdom
def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    datakeys = theJSON.keys()
    mtdata = list(theJSON[country])
    # print(mtdata)

    print(f'Covid stats for {country} (last four days)')
    print(f"Date:\t\tConfirmed:\t\tDeaths:\t\t\tRecoveries:")
    last_for = [-4, -3, -2, -1]
    for i in last_for:
        fmt_data = mtdata[i]
        print(f"{fmt_data['date']}\t\t\t{format(fmt_data['confirmed'], ',d')}\t\t\t{format(fmt_data['deaths'], ',d')}\t\t\t{format(fmt_data['recovered'], ',d')}")
    activecases = 0
    activecases = format((mtdata[-1]['confirmed']) - (mtdata[-1]['deaths']) - (mtdata[-1]['recovered']), ',d')
    print(f"Total number of active cases: {activecases}")


# Open the URL and read the data
webUrl = urllib.request.urlopen(urlData)
# print("result code: " + str(webUrl.getcode()))
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
else:
    print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
