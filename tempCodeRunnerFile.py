hour = int(input("Hour:"))
minute = int(input("minute:"))
total = 0 


for i in range (hour):
    if hour > 1:
        total += 1
    elif minute >= 1:
        total += 1
    else:
        total += 0