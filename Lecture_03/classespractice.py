class Load():
    def __init__(self, max:int):
        self.maxLoad = max
        self.curLoad = 0

    def addLoad(self, load:int)->bool: 
        if (self.curLoad + load > self.maxLoad):
            return False
        else:
            self.curload = load + self.curLoad
            return True 
        


myLoadPlat1 = Load(15)
myLoadPlat2 = Load(10)

if myLoadPlat1.addLoad(20):
    print("WE added it")
else: print("Too much load")
