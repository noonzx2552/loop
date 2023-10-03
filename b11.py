shopping = int(input("shopping:"))
hour = int(input("Hour:"))
minute = int(input("minute:"))

total = 0
if minute >= 1:
    total_min = 30
else:
    total_min = 0

if hour >= 1:
    total_hr = hour*30
else:
    total_hr = 0

if shopping >= 1000:
    total = total_hr+total_min-120
else:
    total = total_hr+total_min-30

if total >= 160:
    total = 150
else:
    total = total
print(total)
