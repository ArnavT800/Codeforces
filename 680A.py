f = list(map(int, input().split(" ")))
d ={}
s = 0
for i in f:
    s+=i
    if i not in d:
        d[i] = 1
    else:
        d[i]+=1
for i in d:
    if d[i]>1:
        if d[i] >3:
            d[i]= i*3
        else:
            d[i] = i*d[i]
diff = 0
for i in d:
    if d[i] !=1 and d[i]>diff:
        diff = d[i]
s-=diff
print(s)
