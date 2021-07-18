# Strings

a = 'Hello how are you?'
print(type(a))

# index in string
print(a[8])

# looping through a string
for e in a:
    print(e)

# string length
print(len(a))

# string slicing
print(a[5:8])
print(a[1:])
print(a[:7])
print(a[-3:])

# string modify
# to upper case
print(a.upper())

# to lower case
print(a.lower())

# remove white space
print(a.strip())

# replace
print(a.replace('e', 'x'))

# string concatenation
b = ' I am good'
print(a + b)

# string format using {} as placeholder and format method
c = 'How old are you? {}'
d = 18
print(c.format(d))

