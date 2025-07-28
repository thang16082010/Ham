def count(str):
    a=str.split()
    print(len(a))
def nguoc(str):
    return (str[::-1])
def check(str):
    if str==nguoc(str):
        print("yes")
    else:
        print("no")
str=input()
count(str)
print(nguoc(str))
check(str)

