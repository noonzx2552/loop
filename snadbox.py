# รับค่าจำนวนนักเรียนทั้งหมด
total_students = int(input("ป้อนจำนวนนักเรียนทั้งหมด: "))

# กำหนดตัวแปรสำหรับนับนักเรียนในแต่ละกลุ่ม
group_a_count = 0
group_b_count = 0
group_c_count = 0

# ใช้ลูปเพื่อแบ่งนักเรียนเป็น 3 กลุ่ม
for i in range(1, total_students + 1):
    if i % 3 == 1:
        group_a_count += 1
    elif i % 3 == 2:
        group_b_count += 1
    else:
        group_c_count += 1

# แสดงผลลัพธ์
print(f"จำนวนนักเรียนในกลุ่ม A: {group_a_count} คน")
print(f"จำนวนนักเรียนในกลุ่ม B: {group_b_count} คน")
print(f"จำนวนนักเรียนในกลุ่ม C: {group_c_count} คน")
