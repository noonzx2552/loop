x = int(input("ต้องการเเลกเงินเท่าไหร่:"))
total = x/2
bank50 = 0
bank20 = 0
coin10 = 0
coin5 = 0
coin2 = 0 
coin1 = 0
#-------------------#
bank20 = x % 50
#-------------------#
coin5 = x % 10
coin2 = coin5 % 5
coin1 = coin2 

print("bank20")