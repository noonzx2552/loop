hour = int(input("Hour:"))
minute = int(input("minute:"))
total = 0 
loop = hour + 1

for i in range (loop):
    if hour >= 1:
        if hour <= 1:
            total += 0
        else:  
            total += 30
    elif minute == 0:
        total += 0
    elif minute >= 1:
        total += 30
    else:
        total += 0

total = total - 30
print(total)
