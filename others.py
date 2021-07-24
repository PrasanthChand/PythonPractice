# With a given tuple, write a program to print the first half values in one line and the last half values in one line.
tup = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
le = int(len(tup)/2)
print(tup[:le])
print(tup[le:])

# a program that accepts a string as input to print "Yes" if string is "yes" or "YES" or "Yes", else print "No".


x = input("say yes or no")

if x == "yes" or "YES" or "Yes":
    print("yes")
else:
    print("no")
