n ,h = list(map(int, input().split(" ")))
height = list(map(int, input().split(" ")))
width = n
for i in height:
    if i > h:
        width+=1
print(width)