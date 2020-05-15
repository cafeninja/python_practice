# Covid stats testing
import urllib.request  # instead of urllib2 like in Python 2.7
import json

urlData = "https://pomber.github.io/covid19/timeseries.json"
country = "US"
country_pop = "United States"

# county names = Malta, Italy, US, United Kingdom
active_cases = 0
def printResults(data):
    # Use the json module to load the string data into a dictionary
    theJSON = json.loads(data)

    datakeys = theJSON.keys()
    mtdata = list(theJSON[country])
    #print(mtdata)

    print(f'Covid stats for {country} (last four days)')
    print(f"Date:\t\tConfirmed:\t\tDeaths:\t\t\tRecoveries:")
    last_for = [-4, -3, -2, -1]
    for i in last_for:
        fmt_data = mtdata[i]
        print(f"{fmt_data['date']}\t\t\t{format(fmt_data['confirmed'], ',d')}\t\t\t{format(fmt_data['deaths'], ',d')}\t\t\t{format(fmt_data['recovered'], ',d')}")
    active_cases = float(mtdata[-1]['confirmed']) - (mtdata[-1]['deaths']) - (mtdata[-1]['recovered'])
    activecases = format((mtdata[-1]['confirmed']) - (mtdata[-1]['deaths']) - (mtdata[-1]['recovered']), ',d')
    print(f"Total number of active cases: {activecases}")



    #---------
    with open('2020.population.country.json', 'r') as myfile:
        popjson = myfile.read()
    #print(popdata)

    #------
    # Use the json module to load the string data into a dictionary
    #theJSON = json.loads(data)

    #datakeys = theJSON.keys()
    #mtdata = list(theJSON[country])
    # print(mtdata)
# ------  End Population --------
    with open('2020.population.country.json', 'r') as myfile:
        popjson = myfile.read()
    # print(popjson)

    # Use the json module to load the string data into a dictionary
    strjson = json.loads(popjson)
    pop = 0
    jsonlist = list(strjson['data'])
    for i in jsonlist:
        if i['name'] == country_pop:
            pop = float(i['pop2020'])
            pop = int(pop * 1000)
            print(f"Population of {country_pop}: {format(int(pop), ',d')}")
            print(f"Current population infected: {format((float(active_cases / pop) * 100), '.4f')}%")



#------  End Population --------


# Open the URL and read the data
webUrl = urllib.request.urlopen(urlData)
# print("result code: " + str(webUrl.getcode()))
if (webUrl.getcode() == 200):
    data = webUrl.read()
    # print out our customized results
    printResults(data)
else:
    print("Received an error from server, cannot retrieve results " + str(webUrl.getcode()))
