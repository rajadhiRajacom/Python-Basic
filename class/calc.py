class calc:
   def __init__(self, num1,num2):
    self.num1 = num1
    self.num2 = num2
   def add(self):
    return self.num1+self.num2
   def sub(self):
    return self.num1 - self.num2
   def mul(self):
    return self.num1 * self.num2
   def div(self):
    return self.num1 / self.num2
c = calc(5000,600)
print(c.add())
print(c.sub())
print(c.mul())
print(c.div())