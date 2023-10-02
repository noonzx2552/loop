student = int(input("นักเรียนทั้งหมด:"))

group1 = 0
group2 = 0
group3 = 0

for i in range(0,student):
    if i % 3 == 1:
        group1 += group1 + 1  
    elif i % 2 == 1:
        group2 += group2 +1
    else:
        group3 += group3 + 1

print("groupA:",group1)
print("groupB:",group2)
print("group3:",group3)