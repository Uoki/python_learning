
a=int(input("請輸入一個正整數(<10):"))
tt=0
for i in range(1,a+1):
  for j in range(1,i+1):
    tt=i*j
    print("%2d" %(tt),end=" ")
  print()