all = int(input("นักเรียนทั้งหมดมีกี่คน:"))
student = int(input("คุณอยู่ลำดับที่เท่าไหร่:"))

if student % 3 == 1:
    print("คุณอยู่:groupA")
elif student % 3 == 2:
    print("คุณอยู่:groupB")
else:
    print("คุณอยู่:groupC")

if all % 3 == 1:
    print("คนสุดท้ายอยู่:groupA")
elif all % 3 == 2:
    print("คนสุดท้ายอยู่:groupB")
else:
    print("คนสุดท้ายอยู่:groupC")
