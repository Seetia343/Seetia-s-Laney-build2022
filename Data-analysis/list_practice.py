US_cities = ["Oakland", "Atlanta", "New York City","Seattle", "Memphis", "Miami", "Boston", "Los Angeles", "Denver", "New Orleans"]

#three_cities= US_cities[0:2]
#print(three_cities)

US_cities[0] = "San Francisco"
US_cities[2] = "Brooklyn"
US_cities[7] = "Hollywood"
US_cities[5] = "Tampa"
#print(CityList)

US_cities.append("New Jersey")
US_cities.extend(["Santa Cruz", "Selma", "Chicago"])
US_cities.insert(7, "Washington", "D.C.")


del US_cities[3]
US_cities.pop(6)
US_cities.remove("New York City")
#deleting 
del US_cities[5]
del US_cities[0]
del US_cities[8]



#US_ciites = CityList[4:8]
#print(US_cities)

#RestaurantList = ["Bento&Bowls","burger king","T4","panda","chickfila","Evert Jone","Prima","Piedology","Boston Market","Taqueria"]
#print(RestaurantList[1])

#technologiesList =["Phone","Laptop","Tv","Game console"]
#print(technologiesList)