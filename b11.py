shopping = int(input("shopping:"))
hour = int(input("Hour:"))
minute = int(input("minute:"))
total = 0 
loop = hour + 1

for i in range (loop):
    if hour >= 1:
        total += 30
    elif minute == 0:
        total += 0
    elif minute >= 1:
        total += 30
    else:
        total += 0
#-------------------------#
if shopping >= 1000:
    total = total - 120
else:
    total = total - 30
#-------------------------#
if total >= 160:
    total = 150
else:
    total = total 
#-------------------------#
if total <= 0:
    print("you have to pay for park Free!.")
else:
    print(f"you have to pay for park {total} bath")