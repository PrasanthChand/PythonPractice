# tuples

# create a tuple using ()
myTuple = (3, 4, 5, 3, 56, 66)

# create a tuple with one item using (,)
singleTuple = ('hello',)

# access items in tuple using index
print(myTuple[1])

# looping through tuple
for x in myTuple:
    print(x)

# join tuples
myTuple1 = (2, 3, 4, 5, 67)
newTuple = myTuple1 + myTuple
print(newTuple)

# multiply tuples
print(newTuple*2)

# count items in tuples
tupCount = newTuple.count(3)
print(tupCount)