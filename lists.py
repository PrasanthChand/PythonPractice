# list

# create a list
myList = ['apple', 'orange', 'mango', 'strawberry']

# print the list
print(myList)

# print items of list based on index
print(myList[0])
print(myList[3])
print(myList[2])

# change items
myList[1] = 'pineapple'
print(myList)

# insert items to list
myList.insert(3, 'cherry')
print(myList)

# pop
myList.pop(1)
print(myList)

# loop through list
for x in myList:
    print(x)

# sorting list - ascending
myList.sort()
print(myList)

# sorting list - descending
myList.sort(reverse=True)
print(myList)

# copy list
newList = myList.copy()
print(newList)

# join lists
list2 = [1, 2, 4, 5, 6]
myList.extend(list2)
print(myList)


