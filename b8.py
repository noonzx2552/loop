import random

visittime1 = 0 #ขนม
visittime2 = 0 #การ์ตูน
visittime3 = 0 #เกมส์

time1 = 0
time2= 0
time3 = 0

days = ["Mon","Tus","wen","thi","fri"]

for day in days:
    shop =random.choice(["visittime1", "visittime2", "visittime3"])
    if days == "wen":
        if shop == "visittime1":
            visittime1 += 1
            time1 += 5
        elif shop == "visittime2":
            visittime2 += 1
            time2 += 10
        else:
            visittime3 += 1
            time3 += 30
    else:
        for i in range(2):
        #shop = random.choice(["visittime1", "visittime2", "visittime3"])
            if shop == "visittime1":
                visittime1 += 1
                time1 += 5
            elif shop == "visittime2":
                visittime2 += 1
                time2 += 10
            else:
                visittime3 += 1
                time3 += 30

print(f"ร้านขนม:{visittime1} ครั้ง / ร้านการ์ตูน:{visittime2} ครั้ง / ร้านเกมส์:{visittime3} ครั้ง")
print(f"เวลาเข้าร้านขนม:{time1} นาที / เวลาเข้าร้านการ์ตูน:{time2} นาที / เวลาเข้าร้านเกมส์:{time3} นาที")

