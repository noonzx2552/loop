import random

visittime1 = 0 #ขนม
visittime2 = 0 #การ์ตูน
visittime3 = 0 #เกมส์
visittime4 = 0 #ร้านbeauty

time1 = 0
time2= 0
time3 = 0
time4 = 0

days = ["Mon","Tus","wen","thi","fri","sat"]

for day in days:
    if day == "wen":
        shop =random.choice(["visittime1", "visittime2", "visittime3","visittime4"])
        print(f"วันพุธ:{shop}")
        print("------------------------------")
        if shop == "visittime1":
            visittime1 += 1
            time1 += 5
        elif shop == "visittime2":
            visittime2 += 1
            time2 += 10
        elif shop == "visittime3":
            visittime3 += 1
            time3 += 30 
        else:
            visittime4 += 1
            time4 += 45
    elif day == "sat":#ห้ามเข้าร้านshop1
        for i in range(2):
            shop_1 =random.choice(["visittime2", "visittime3","visittime4"])
            print(f"วันเสาร์:{shop_1}")
            print("------------------------------")
            if shop_1 == "visittime2":
                visittime2 += 1
                time2 += 10
            elif shop_1 == "visittime3":
                visittime3 += 1
                time3 += 30
            else:
                visittime4 += 1
                time4 += 45
    else:
        for i in range(2):
            shop_2 =random.choice(["visittime1", "visittime2", "visittime3","visittime4"])
            print(f"day: {day} {shop_2}")
            if shop_2 == "visittime1":
                visittime1 += 1
                time1 += 5
            elif shop_2 == "visittime2":
                visittime2 += 1
                time2 += 10
            elif shop_2 == "visittime3":
                visittime3 += 1
                time3 += 30
            else:
                visittime4 += 1
                time4 += 45

print(f"ร้านขนม:{visittime1} ครั้ง / ร้านการ์ตูน:{visittime2} ครั้ง / ร้านเกมส์:{visittime3} ครั้ง /เข้าร้านbeauty:{visittime4} ครั้ง")
print(f"เวลาเข้าร้านขนม:{time1} นาที / เวลาเข้าร้านการ์ตูน:{time2} นาที / เวลาเข้าร้านเกมส์:{time3} นาที / เวลาเข้าร้านbeauty:{time4} นาที")
