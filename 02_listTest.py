win = ['NT', 'xp','2008', '2010',10]
print(win[0])
win.append('2020')
print(win[4])
win.append(input("Enter windows"))
win.insert(0,'win0')
win.insert(-1,'win1')
win.append("555")
print(win.__len__())
print(win)
print(win.pop(1))
print(win)
print (win.remove('xp'))
print(win)
print (win.reverse())
print(win)
for w in win:
    print(w)
if '3030' in win:
    print("3030 is present")
    
i = [1,2,3,4,5]
j = ['a','b','c','d']
print(i)
i.append(j)
i.append('test')
print(i)
print(i+j)
print( len(i))
print( len(j))