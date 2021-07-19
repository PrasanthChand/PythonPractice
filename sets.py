# sets

# create a set using {}
mySet = {2, 'apple', 4, 34, ' '}
print(mySet)

# set length
print(len(mySet))

# add an item to set
mySet.add(35)
print(mySet)

# remove an item from set
mySet.remove('apple')
print(mySet)

# loop through set
for x in mySet:
    print(x)

# join two sets using union
mySet1 = {2, 34, 26, 65}
newSet = mySet.union(mySet1)
print(newSet)

# join two sets using update
mySet.update(mySet1)
print(mySet)

# intersection_update method - keeps only the items that are present in both sets.
set1 = {1, 2, 3, 4}
set2 = {2, 3, 5, 6}
set1.intersection_update(set2)
print(set1)

# intersection method - returns a new set with items that are present in both sets.
set3 = set1.intersection(set2)
print(set3)

# symmetric_difference_update method - keeps only the elements that are NOT present in both sets
set1.symmetric_difference_update(set2)
print(set1)

# symmetric_difference method - return a new set, that contains only the elements that are NOT present in both sets
set4 = {'a', 'b', 'c', 'd'}
set5 = {'b', 'd', 'e', 'g'}
x = set4.symmetric_difference(set5)
print(x)


