i = int(input('what is size required'))
for a in range(i,0,-1):
    for j in range(i,0,-1):
        if a>j:
            print("*", end=" ")
        elif a==j:
            print("-", end=" ")
        else:
            print("*", end=" ")
    print()