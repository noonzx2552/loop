hour = int(input("Hour:"))
minute = int(input("minute:"))
total_min = 0 
total_hr = 0
if minute >= 1:
    total_min = 30
else:
    total_min = 0

if hour >= 1:
    total_hr = hour*30
else:
    total_hr = 0
total = total_min + total_hr - 30
print(total)