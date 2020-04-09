import math
t = int(input())
l = []
for i in range(t):
    n = int(input())
    ll = [n-1, 1]
    l.append(ll)
for i in l:
    print(*i)