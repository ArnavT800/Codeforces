m, d = list(map(int, input().split(" ")))
if m == 2:
    e = 28
    e+=d-1
    if e%7!= 0:
        print(int(e//7 +1))
    else:
        print(int(e/7))
elif m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12:
    e = 31
    e+=d-1
    if e%7!= 0:
        print(int(e//7 +1))
    else:
        print(int(e/7))
else:
    e = 30
    e+=d-1
    if e%7!= 0:
        print(int(e//7 +1))
    else:
        print(int(e/7))


