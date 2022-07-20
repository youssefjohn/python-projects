mydict = {}

mydict["Youssef"] = 16
print(mydict)

mydict["Youssef"] = 32
print(mydict["Youssef"])

mydict["Ahmed"] = 32
mydict["Dennis"] = 31

print(mydict)

for key in mydict:
    print(mydict[key])


travel_log = {
    'France': ['paris', 'dijon']
}


travel_log['cities_visited'] = {'Paris': 2, 'Dijon': 4}
print(travel_log)