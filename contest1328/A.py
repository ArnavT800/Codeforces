t = int(input())
for i in range(t):
    k = 0
    a,b = map(int, input().split(" "))
    if a%b == 0:
        k = 0
    else:
        k+=b-(a%b)
    print(k)