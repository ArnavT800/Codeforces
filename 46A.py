n = int(input())
f = 1
i = 1
a = []
t = 0
while t!= n-1 :
    f+=i
    if f > n:
        f = f-n
    a.append(f)
    i+=1
    t+=1
a = " ".join(map(str, a))
print(a)
