def giaithua(n):
    res=1
    for i in range(1,n+1):
        res*=i
    print(res)
n=int(input())
giaithua(n)