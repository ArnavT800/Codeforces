n = int(input())
po = list(map(int, input().split(" ")))
curOff = 0
unt = 0
for i in po:
    if i!=-1:
        curOff+=i
    else:
        if curOff==0:
            unt+=1
        else:
            curOff+=i
print(unt)
        