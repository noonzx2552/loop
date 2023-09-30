x = int(input("x:"))

total = 0

for i in range(1,x+1):
    if i % 10 != 0:
        total += i
    
    print(total)