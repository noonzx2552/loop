while True:
    # รับ input จำนวนชั่วโมงและนาที
    hour = int(input("ป้อนจำนวนชั่วโมง (หยุดโปรแกรมโดยป้อน -1): "))
    
    # ถ้าผู้ใช้ป้อน -1 ให้ออกจากลูป
    if hour == -1:
        break

    minute = int(input("ป้อนจำนวนนาที: "))

    # คำนวณค่าที่จอดรถ
    total_hours = hour + (minute // 60)  # รวมชั่วโมงและเศษนาทีเป็นชั่วโมง
    if total_hours <= 1:
        parking_fee = 0  # ชั่วโมงแรกจอดฟรี
    else:
        parking_fee = (total_hours - 1) * 30  # ค่าจอดชั่วโมงละ 30 บาท

    # แสดงค่าที่จอดรถ
    print(f"ค่าที่จอดรถ: {parking_fee} บาท")