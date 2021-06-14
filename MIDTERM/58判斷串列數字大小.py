list1=[]
list2=[]
list3=[]

for i in range(1,11):
    data1 = int(input("請輸入第"+str(i)+"個數字:"))
    list1.append(data1)

for i in range(1,4):
    data2 = max(list1)
    list2.append(data2)
    list1.remove(data2)
for j in range(1,4):
    
    data3 = min(list1)
    list3.append(data3)
    list1.remove(data3)
list2.sort(reverse=True)
list3.sort(reverse=True)
print("最大的3個數字為："+str(list2))
print("最小的3個數字為："+str(list3))