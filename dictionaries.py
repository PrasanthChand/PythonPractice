# dictionaries

myDict = {
    "A": "Java",
    "B": "Python",
    "C": "JavaScript",
    "D": "GoLang",
    "E": "C"
}

print(myDict)

# access the values of the Dictionary items
print(myDict["B"])

# show the length of the dictionary
print(len(myDict))

# show the type of the dictionary
print(type(myDict))

# key() method to display all the keys in a dictionary
print(myDict.keys())

# values() method to display all the values in a dictionary
print(myDict.values())

# items() method to display the items of dictionary in a tuple
print(myDict.items())

# change values of items in a dictionary
myDict["E"] = "nodeJS"
print(myDict)

# pop() method to remove an item from the dictionary
myDict.pop("D")
print(myDict)

# loop through items in a dictionary and print all keys
for x in myDict:
    print(x)

# loop through items in a dictionary and print all values using values() method
for x in myDict.values():
    print(x)

# copy contents of a dictionary to a new dictionary
newDict = myDict.copy()
print(newDict)
