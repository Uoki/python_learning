a=int(input("請輸入一個度數："))
if a<=120:
    print("Summmer months:"+str(2.1*a))
    print("Non-Summmer months:"+str(2.1*a))
elif a>=121 and a<=330:
    print("Summmer months:"+str(120*2.1+(a-120)*3.02)) 
    print("Non-Summmer months:"+str(120*2.1+(a-120)*2.68)) 
elif a>=331 and a<=500:
    print("Summmer months:"+str(120*2.1+210*3.02+(a-330)*4.39))
    print("Non-Summmer months:"+str(120*2.1+210*2.68+(a-330)*3.61))
elif a>=501 and a<=700:
    print("Summmer months:"+str(120*2.1+210*3.02+170*4.39+(a-500)*4.97))
    print("Non-Summmer months:"+str(120*2.1+210*2.68+170*3.61+(a-500)*4.01))
else:
    print("Summmer months:"+str(120*2.1+210*3.02+170*4.39+200*4.97+(a-700)*5.63))
    print("Non-Summmer months:"+str(120*2.1+210*2.68+170*3.61+200*4.01+(a-700)*4.5))