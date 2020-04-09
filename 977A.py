t = input().split(" ")
n = int(t[0])
k = int(t[1])

for i in range(k):
    if n%10 == 0:
        n = n/10
    else:
        n-=1

print(int(n))
    

