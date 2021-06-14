class Univerity:
    def __init__(self,name):
        self.cps=[]
        self.name=name
class campus:
    def __init__(self,name):
        self.dps =[]
        self.name=name
class department:
    def __init__(self,name):
        self.name=name

data ={"建工校區":["機械","電子","電機","化材","土木"],
       "燕巢校區":["智商","金資","會資","財稅","觀光"],
       "第一校區":["資工","運籌","資管","外語","營建"],
       "楠梓校區":["商資","供管","海管","水產","海生"],
       "旗津校區":["電工","航運","海資","輪機","海工"]}
nkust=Univerity("國立高雄科技大學")
n=-1

for key,value in data.items():
    nkust.cps.append(campus(key))
    n+=1
    for i in value:
        nkust.cps[n].dps.append(department(i))