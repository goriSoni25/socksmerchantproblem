from collections import Counter
from array import*
ar= [10,10,10,10,20,30,30,30,30,30,30,30,40,40,40,40,40]
#for counting the frequency of particular color
count = Counter(ar)
print("count",count)
value= count.values()
print(value)
print("countvalues",value)
pairs=0
for i in value:
    pairs=pairs+i//2
print("total pairs rohit can sell",pairs) 