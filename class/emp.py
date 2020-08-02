class emp:
    
    company = 'HCL'
    sal = '100'
    def fullName(self, firstname, LastName):
        return firstname + " " + LastName
    
    def getName(self):
        return self.company
    def getSalary(self):
        return self.sal
        


class manager(emp):
    salary = '10000000'
    
    def getSalary(self):
        self.defaultSal=super().sal
        return self.salary
        
class engineer(emp):
    salary = '2000000'
    
    def getSalary(self):
        return self.salary

f = manager()
print(type(f))
print(f.fullName("Raja", "Muthu"))
print(f.company)
print(f.getName())
print(f.getSalary())
print("default salary",f.defaultSal )


e = engineer()
print(type(e))
print(e.fullName("Robert", "Kumar"))
print(e.company)
print(e.getName())
print(e.getSalary())







