import math
n = int(input())
w = [1, 1]
b = [n, n]
x,y = list(map(int, input().split(" ")))
wdist = math.sqrt((y-w[1])**2 + (x-w[0])**2)
bdist = math.sqrt((y-b[1])**2 + (x-b[0])**2)

if wdist<=bdist:
    print("White")
else:
    print("Black")