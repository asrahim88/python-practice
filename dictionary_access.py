dictionary = {
    "name": "Abdur rahim",
    "id": 456,
    "phone": "016587945321",
    "year" : 2022
}

print(type(dictionary))
print(dictionary)

#convert to list
print(list(dictionary.keys()))
print(list(dictionary.values()))

#convert to tuple
print(tuple(dictionary.keys()))
print(tuple(dictionary.values()))

#convert to set 
print(set(dictionary.keys()))
print(set(dictionary.values()))

# access dictionary 1st way
print(dictionary["name"])
print(dictionary["id"])
print(dictionary["phone"])

#access dictionary 2nd way
print(dictionary.get("name"))
print(dictionary.get("id"))
print(dictionary.get("phone"))

#access dictionary 3rd way 
print(dictionary.keys())
print(dictionary.values())

#access dictionary 4th way
print(dictionary.items())


#check iem in dictionary using keys
if "id" in dictionary:
    print("yes")