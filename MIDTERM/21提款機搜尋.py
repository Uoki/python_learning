n=int(input("輸入查詢組數N為："))
dict1={"123 456":"9000","456 789":"5000","789 888":"6000",
       "336 558":"10000","775 666":"12000","566 221":"7000"}
list1=[]
for i in range(1,n+1):
    code=input("")
    list1.append(dict1.setdefault(code,"error"))
for j in range(1,n+1):
    if code in dict1 :        
        print(list1[j-1])
    else:
        print("error")