# for loop demo - prints pattern similar to below, based on size given by user
#   - * * * * * *
#   * - * * * * *
#   * * - * * * *
#   * * * - * * *
#   * * * * - * *
#   * * * * * - *
#   * * * * * * -

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

# while loop demo - to check under or over weight

i = int(input('what is the weight'))
while i<=50:
    print('under weight')
else:
    print('over weight')

