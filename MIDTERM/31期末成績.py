


chi=int(input("國文:"))
eng=int(input("英文:"))
math=int(input("微積分:"))
pe=int(input("體育:"))
code=int(input("程式設計:"))
avg=round((chi+eng+math+pe+code)/5,2)

print("平均分數:"+str(avg))

dict1={chi:"國文",eng:"英文",math:"微積分",pe:"體育",code:"程式設計"}

list1=[chi,eng,math,pe,code]

mmm=max(list1)
nnn=min(list1)
print("最高分科目:"+str(dict1[mmm])+str(mmm)+"分")
print("最低分科目:"+str(dict1[nnn])+str(nnn)+"分")