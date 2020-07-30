def lenSort(length):
       return len(length)
def nameSort(length):
       return len(length)       
       
       
win=['Wins10','wins2020','NT','winXp', 'win3030',"W"]
win.sort(reverse=True,key=lenSort)
print(win)
win.sort(reverse=False,key=lenSort)
print(win)