n = int(input())
c = list(map(int, input().split(" ")))
maxList = []
minList = []
for i in range(n):
    x = 0
    diff = []
    while x<len(c):
        sub = abs(c[i] - c[x])
        diff.append(sub)
        x+=1
    maxList.append(max(diff))
    diff.remove(min(diff))
    minList.append(min(diff))

for i in range(len(maxList)):
    print(minList[i], maxList[i])
