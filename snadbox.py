# รับจำนวนแบงค์ 100, 500, และ 1000
num_1000 = int(input("จำนวนแบงค์ 1000 บาท: "))
num_500 = int(input("จำนวนแบงค์ 500 บาท: "))
num_100 = int(input("จำนวนแบงค์ 100 บาท: "))

# คำนวณจำนวนแบงค์ย่อยและเหรียญ 50 บาท
num_50_coins = 0
num_20_coins = 0
num_10_coins = 0
num_5_coins = 0

# คำนวณจำนวนแบงค์ 1000 บาทที่สามารถแลกเป็นแบงค์ย่อย
num_1000_to_500 = num_1000 * 2

# คำนวณจำนวนแบงค์ 500 บาทที่สามารถแลกเป็นแบงค์ย่อย
num_500_to_100 = num_500 * 5

# คำนวณจำนวนแบงค์ 100 บาทที่สามารถแลกเป็นแบงค์ย่อย
num_100_to_50 = num_100 * 2

# รวมแบงค์ 1000 บาท, 500 บาท และ 100 บาท ที่สามารถแลกเป็นแบงค์ย่อย
total_banknotes_to_coins = num_1000_to_500 + num_500_to_100 + num_100_to_50

# แบงค์ 1000 บาท, 500 บาท, และ 100 บาท ที่ไม่สามารถแลกเป็นแบงค์ย่อย
num_1000_left = num_1000 - num_1000_to_500
num_500_left = num_500 - num_500_to_100
num_100_left = num_100 - num_100_to_50

# คำนวณจำนวนแบงค์ย่อยและเหรียญตามจำนวนที่ได้
while total_banknotes_to_coins >= 50:
    if total_banknotes_to_coins >= 50:
        num_50_coins += 1
        total_banknotes_to_coins -= 50
    if total_banknotes_to_coins >= 20:
        num_20_coins += 1
        total_banknotes_to_coins -= 20
    if total_banknotes_to_coins >= 10:
        num_10_coins += 1
        total_banknotes_to_coins -= 10
    if total_banknotes_to_coins >= 5:
        num_5_coins += 1
        total_banknotes_to_coins -= 5

# แสดงผลลัพธ์
print(f"แบงค์ 1000 บาทที่แลกเป็นแบงค์ย่อย: {num_1000_to_500} แบงค์")
print(f"แบงค์ 500 บาทที่แลกเป็นแบงค์ย่อย: {num_500_to_100} แบงค์")
print(f"แบงค์ 100 บาทที่แลกเป็นแบงค์ย่อย: {num_100_to_50} แบงค์")
print(f"แบงค์ 1000 บาทที่ไม่สามารถแลกเป็นแบงค์ย่อย: {num_1000_left} แบงค์")
print(f"แบงค์ 500 บาทที่ไม่สามารถแลกเป็นแบงค์ย่อย: {num_500_left} แบงค์")
print(f"แบงค์ 100 บาทที่ไม่สามารถแลกเป็นแบงค์ย่อย: {num_100_left} แบงค์")
print(f"จำนวนเหรียญ 50 บาท: {num_50_coins} เหรียญ")
print(f"จำนวนเหรียญ 20 บาท: {num_20_coins} เหรียญ")
print(f"จำนวนเหรียญ 10 บาท: {num_10_coins} เหรียญ")
print(f"จำนวนเหรียญ 5 บาท: {num_5_coins} เหรียญ")