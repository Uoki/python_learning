m=int(input("請輸入階層值M："))
total=n=1
while(m>total):
    total=total*n
    n+=1
print("超過M為"+str(m)+"的最小階層N值為:"+str(n-1))