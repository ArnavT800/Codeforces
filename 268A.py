n = int(input())
zero = []
one = []
count = 0
for i in range(n):
    j = list(map(int, input().split(" ")))
    zero.append(j[0])
    one.append(j[1])

for i in zero:
    count+=one.count(i)
print(count)

