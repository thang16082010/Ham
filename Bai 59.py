def square(n):
    print(n**2)
def rec(n,m):
    print(n*m)
def cir(n):
    print(round(n*n*3.14,2))
a,b,c,d=map(int,input().split())
square(a)
rec(b,c)
cir(d)