import math
def ktsnt(n):
    if n<2:
        return 0
    for i in range(2,int(math.sqrt(n))+1):
        if n%i==0:
            return 0
    return 1
n=int(input())
if ktsnt(n)==1:
    print("yes")
else:
    print("no")