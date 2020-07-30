cmp =  {"HCL","InfoSys","ITC","TechMach"}
print(cmp)

pin = set((566011,560001,"789789",9982349))
print("Pin ", pin)
cmp.add("ITC")

#Bulk update
cmp.update(["DELL","HP","Lenovo"])
print(cmp)

print("Length", len(cmp))

#Remove error out if ele is not present (will not move to next step) but discard will not error out
#print(cmp.remove("ABB")) 
print(cmp.discard("ABB"))

print("Removed Item", cmp.pop())
print("After removed",cmp)

print("clear" , cmp.pop())
print("After cleared",cmp)

#if use print after del, NameError: name 'cmp' is not defined 
#del cmp
#print("After Deleted ", cmp)
print("------------------------------")
num = {1,2,3,4,5,6,7}
alph = {"a","b","c","d",1,5,6,7}

u1 = num.union(alph)
i1 = num.intersection(alph)
i1.intersection_update(num)

print("num set ", num)
print("Alph set ", alph)
print("Union set (all) ", u1)
print("Intersection set (only common)", i1)
print("Intersection update", i1)

print("num issubset inters", num.issubset(i1))
print("num issubset union", num.issubset(u1))

print("num issuperset inters", num.issuperset(i1))
print("num issuperset union", num.issuperset(u1))


print("------------------------------")

num1 = {10,20,30,90}
num2 = {100,200,30,90}
num3 = num1.difference(num2)
print("num1", num1)
print("num2", num2)
print("num3", num3)

print("difference of num1 and num2", num3)

print("only difference is stored in num1", num1.difference_update(num2))
print("num1", num1)
print("num2", num2)
print("num3", num3)

num4 = num1.symmetric_difference(num2)
print("except same values ", num4)
print("except same values ", num1.symmetric_difference_update(num2))
print("num1", num1)
print("num2", num2)
print("num3", num3)
