class Mobile:
    _model ="Samsung"  #protected
    cost = "$ 188888"  #public
    __madein = "India"  #private
    
    def getModel(self):
       return self._model
    def getCost(self):
        return self.cost
    def getMadein(self):
        return self.__madein
    def _batter(self):
        return "SAMSUNG BAT-10001"
    def __CPU(self):
        return "AND CPU 1003"
        
class Nokia(Mobile):
    def nokiaConfig(self):
        return "Nokia 10098"
    def getModel(self):
       return "Nokia 1000"
    def getCost(self):
        return "Rs 5555555"
    def _batter(self):
        return "Nokia BAT-10001"

        
sam = Mobile()
print(sam._model)
print(sam.cost)
#print(sam.__madein)
print(sam.getMadein())

print(sam._batter())
#print(sam.__CPU())

nokia = Nokia()
print(nokia.getModel())
print(nokia.getCost())
#print(sam.__madein)
print(nokia.getMadein())

print(nokia._batter())
#print(nokia.__CPU())

