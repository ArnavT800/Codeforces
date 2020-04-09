t = int(input())
res = []
for i in range(t):
    n = int(input())
    inp = sorted(list(map(int, input().split(" "))))
    unq = set()
    for i in range(n):
        unq.add(inp[i])   
    res.append(len(unq))

for i in res:
    print(i)