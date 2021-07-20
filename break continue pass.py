# break continue pass

for n in range(1, 101):

    if (n % 3 == 0) or (n % 5 == 0):
        continue
        print(n)

    else:
        print(n)

for m in range(1, 101):

    if m % 2 == 0:
        pass

    else:
        print(m)

for q in range(1, 101):

    if q % 2 == 0:
        break

    print(q)

