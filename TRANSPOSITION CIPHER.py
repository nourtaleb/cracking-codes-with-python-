import math 
message = 'common sense is not so common'
translated = ''

key = 8 
numrows=math.ceil(len(message)/key)
l=[]
for i in range (0 , numrows):
    l.append([])
    for j in range (0 , key):
       
        location = j + i * key
        if location < len (message):
            l[i] [j] = message [location]
        else: 
            l [i] [j]=None 
print (l)    