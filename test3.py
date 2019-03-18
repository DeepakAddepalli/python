#dictionary

cities ={"hyd":"040","blr":[80,12,23],"chennai":"044"}

print(len(cities))
print(type(cities))
print(cities.keys())
print(cities.values())
print(cities.items())



#add/modify

cities["pune"]="022"
cities["pune"]="020"

#delete

del cities["blr"]
