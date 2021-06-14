a=input("檢測的字串(end結束)：")
while a!="end":
    b=list(a)
    two=input("檢測的單一字元:")  
    if a!="end":
        a=b.count(two)
        print("字元",two,"出現次數為:",a)
    a=input("檢測的字串(end結束):")
    if a=="end":
        print("檢測結束")