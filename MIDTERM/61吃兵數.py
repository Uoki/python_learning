time = input("請輸入遊戲時間:").split(":")
a =int(time[0])*60 +int(time[1]) - 75
c = 0
c1 = 0
sum1 = 0
while a  >= 30 :
    a = a-30
    c =c + 1
    c1 =c1 +1 
    if c == 3:
        sum1 = sum1+7
        c = 0
    else:
        sum1 = sum1+6
    if c1 == 2:
        sum1 = sum1 - 1
        c1 = 0
print(str(sum1)+"隻兵")