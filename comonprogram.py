from collections import Counter
from array import*
ar= array("i",[])
#enter th no. of socks you want 
n= int(input("no. of socks you want in rohit pile \n"))
for i in range (n):
    #enter the color code for socks
    x= int(input("enter the no. of color \n"))
    ar.append(x)

count = Counter(ar)
print("count",count)
value= count.values()
print()
print("countvalues",value)
pairs=0
for i in value:
    pairs=pairs+i//2
print("total pairs rohit can sell",pairs) 
