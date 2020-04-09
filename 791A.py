l, b = list(map(int, input().split(" ")))
d = 0
while l<=b:
    l*=3
    b*=2
    d+=1
print(d)

