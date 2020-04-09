T = int(input())
xList = []
yList = []
for i in range(T):
    inp = list(map(int, input().split(" ")))
    l = inp[0]
    r = inp[1]
    if r % l == 0:
        xList.append(l)
        yList.append(r)
    else:
        if r-(r%l) != l:
            xList.append(l)
            yList.append(r-(r%l))
        elif l + (r%l) != r:
            xList.append(l+(r%l))
            yList.append(r)
for i in range(len(xList)):
    print(xList[i], yList[i])

