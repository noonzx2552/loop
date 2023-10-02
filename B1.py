student = int(input("นักเรียนทั้งหมด:"))

groupa = 0
groupb = 0
groupc = 0

for i in range(1,student+1):
    if i % 3 == 1:
        groupa += 1  
    elif i % 3 == 2:
        groupb += 1
    else:
        groupc += 1

print("groupA:",groupa)
print("groupB:",groupb)
print("group3:",groupc)