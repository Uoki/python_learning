
class Classroom:
    def __init__(self,clss,sid,name,gh):
        self.clss=clss
        self.sid=sid
        self.name=name
        self.gh=gh

tmp1=[]

fp=open('test.csv',"r") #開啟檔案
tmp=fp.readline()
for i in tmp:
    tmp2=i.split(" ")
    tmp1.append(Classroom(tmp2[0],tmp2[1],tmp2[2],tmp2[3]))

fp.close()
