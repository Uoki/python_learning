a=input("輸入五張牌：")
b=a.split(" ")
c=0
for i in range(5):
    if str(b[i])=="A":
        c+=1
    elif str(b[i])=="J":
        c+=11
    elif str(b[i])=="Q":
        c+=12
    elif str(b[i])=="K":
        c+=13
    else:
        c+=int(b[i])
print(c)