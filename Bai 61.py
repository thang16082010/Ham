def maxmin(a):
    ma=mi=a[0]
    for i in range (0,len(a)):
        ma=max(ma,a[i])
        mi=min(mi,a[i])
    print(ma,mi)
def find(a,n):
    for i in range (0,len(a)):
        if a[i]==n:
            print(i)