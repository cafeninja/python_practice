import json

country = "US"

with open('2020.population.country.json', 'r') as myfile:
    popjson = myfile.read()
# print(popjson)

# Use the json module to load the string data into a dictionary
strjson = json.loads(popjson)
pop = 0
jsonlist = list(strjson['data'])
for i in jsonlist:
    if i['name'] == country:
        pop = float(i['pop2020'])
        pop = pop*1000
        print(f"Population of {country}: {format(int(pop), ',d')}")


# for name in popdata:
#     if name == country:
#         print(f'Matched index with country name.')
#         pop = float(item['pop2020'])
# print(pop)
# pop = pop*1000
# print(f"Population of {country}: {format(int(pop), ',d')}")