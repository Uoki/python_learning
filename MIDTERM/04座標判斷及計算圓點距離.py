x=int(input("請輸入X軸的座標："))
y=int(input("請輸入Y軸的座標："))
z=x**2+y**2
if(x>0 and y>0):
    print("該點位於第一象限，離原點距離為根號"+str(z))
elif(x<0 and y>0):
    print("該點位於第二象限，離原點距離為根號"+str(z))
elif(x<0 and y<0):
    print("該點位於第三象限，離原點距離為根號"+str(z))
elif(x>0 and y<0):
    print("該點位於第四象限，離原點距離為根號"+str(z))
elif(x==0 and y==0):
    print("該點位於原點")
elif(x==0 and y>0):
    print("該點位於上半平面Y軸上，離原點距離為根號"+str(z))
elif(x==0 and y<0):
    print("該點位於下半平面Y軸上，離原點距離為根號"+str(z))
elif(x>0 and y==0):
    print("該點位於右半平面X軸上，離原點距離為根號"+str(z))
elif(x<0 and y==0):
    print("該點位於左半平面X軸上，離原點距離為根號"+str(z))