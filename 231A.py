n = int(input())
count = 0
for i in range(n):
    inp = list(map(int, input().split(" ")))
    if inp.count(1)>=2:
        count+=1
    else:
        continue
print(count)

