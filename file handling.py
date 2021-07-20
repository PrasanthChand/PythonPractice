# file handling

f = open("python.txt", "rt")
print(f.read())
f.close()


#  split() function
with open("file.text", "r") as file:
    data = file.readlines()
    for line in data:
        word = line.split()
        print(word)
file.close()

