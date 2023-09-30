x = int(input(":"))

total = 0

for i in range (1,x+1):
    if i % 3 != 0:
        total += i
    elif i % 7 != 0:
        total += i

    print(total)