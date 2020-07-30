emp = {
 "Name": "Python",
 "Dep": "Lang",
 "Age": 10,
 2:200
 } 
list1 = [1,2,3,4]
print (emp)
if "Python" in emp.values():
    print("Python is present")

for x in emp:
    print (emp[x])
    
for x in emp.keys():
    print (emp[x])
    
for x in emp.values():
    print(x)

for x,y in emp.items():
    print(x,y)

#Fetch the value
print(emp.get(2))
print(emp.get("Name"))
print(emp.get("Lang","Python 3.8"))
print(emp.fromkeys(list1))
print(emp.fromkeys(list1,"Sample"))

#Remove
emp.pop("Name") 
print(emp) 

#it will remove last one
emp.popitem() 
print(emp) 

#Update
emp.update({"Age":200})
print(emp)

emp.update({2:400})
print(emp)

emp.setdefault("Name",'Python default')

emp.setdefault("Name",'Python default1')
print(emp)