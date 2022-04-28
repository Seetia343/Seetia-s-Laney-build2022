#              0           1             2            3         4          5        6           7              8        9
US_cities = ["Oakland", "Atlanta", "New York City","Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]

#three_cities= US_cities[0:2]
#print(three_cities)

US_cities[0] = "San Francisco"
US_cities[2] = "Brooklyn"
US_cities[7] = "Hollywood"
US_cities[5] = "Tampa"
#print(US_cities)
# US_cities = ["San Francisco"", "Atlanta", Brooklyny","Seattle", "Memphis", "Tampa", "Boston", "Holllywood", "Denver", "New Orleans"]

US_cities.append("New Jersey")
US_cities.extend(["Santa Cruz", "Selma", "Chicago"])
US_cities.insert(7, "Washington")

# US_cities = ["San Francisco"", "Atlanta", Brooklyny","Seattle", "Memphis", "Tampa", "Boston", "washington", "Holllywood", "Denver", "New Orleans", "New Jersey", "Santa Cruz", "Selma", "Chicago"]

del US_cities[3]
US_cities.pop(6)
US_cities.remove("New Orleans")
#deleting 
del US_cities[5]
del US_cities[0]
del US_cities[8]

# US_cities = [ "Atlanta", "Brooklyn", "Memphis", "Tampa", "Holllywood", "Denver", "New Jersey", "Santa Cruz", "Chicago"]


#US_ciites = CityList[4:8]
print(US_cities)

#RestaurantList = ["Bento&Bowls","burger king","T4","panda","chickfila","Evert Jone","Prima","Piedology","Boston Market","Taqueria"]
#print(RestaurantList[1])

#technologiesList =["Phone","Laptop","Tv","Game console"]
#print(technologiesList)