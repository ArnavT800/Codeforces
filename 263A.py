s = []
for i in range(5):
    inp = list(map(int, input().split(" ")))
    if inp.count(1) >0:
        ind = inp.index(1)
        s.append(i)
        s.append(ind)

steps = abs(s[0] - 2) + abs(s[1]-2)
print(steps)

