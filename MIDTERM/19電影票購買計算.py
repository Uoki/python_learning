a=int(input("組數為："))
y=[]
z=[]
total=0
for i in range(1,a+1):
    x=str(input("第 "+str(i)+" 組："))
    y=x.split(" ")
    z.append(y)
for i in range(0,a):
    total = 0
    total = int(z[i][0])*250+total
    total = int(z[i][1])*175+total
    print("第 "+str(i+1)+" 組應收費用："+str(total))
