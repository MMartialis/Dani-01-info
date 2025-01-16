class Tree():
    def __init__(self, height:float):
            self.height = height 

class DeciduousTree(Tree):
    def __init__(self, height:float, leafType:int):
        super.__init__(height)   #runnign the __init__(constructor) from class Tree (Main/ssuperclass)
        self.leafType = leafType
class Confire(Tree):
    def __init__(self, height:float, needleLength: float ):
         super.__init__(height)
         self.needleLength = needleLength



class Private():
    def __init__(self, privateVal):
        self.__privateVal = privateVal  #__ makis it a private attribute
    def getPrivateVal(self):
        return self.__privateVal  #return the private attribute, HERE YOU ARE ALLOWED TO READ OR WRITE PRIVATE VARIABLES 
    

myP = Private(20)

pVal = myP.__privateVal   # DONT DO THIS, THIS IS ILLEGAL
pVal = myP.getPrivateVal() # DO THIS instead
         