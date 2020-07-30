
#tuple
win =   ('xp', '2020', '3030', 'NT', 'win8',10,False)
print(win)

copyWin = tuple(win)
print(win.count('xp'))
print(win is copyWin)

#List
os = ('Windows', 'Linux', 'Unix')
print(win.__add__(os))

copyOs = list(os)
print(os is copyOs)

print(win.__len__())
print(len(win))

if "Unix" in os:
    print("Unix is present")
    
for s in os:
    print(s)
    
print(win.__contains__('xp'))
#win[0] = 'test'
#win[8] = True

company = ['HCL','ITC','Capgamni','infoSys','TechMech',False,200]
print(company)
company[0] = 'OnePluse'
print(company)