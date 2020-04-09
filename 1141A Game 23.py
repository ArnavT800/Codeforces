inp = input().split(" ")
n = int(inp[0])
m = int(inp[1])
poss = True
zero = False
steps = 0
if m==n:
    zero = True
elif m%n != 0:
    poss= False   
quot = m/n
if quot%6 == 0 or quot%2 == 0 or quot%3 == 0:
    while quot > 1:
        if quot%2 ==0:
            quot//=2
            steps+=1
        else:
            quot//=3
            steps+=1
else:
    poss = False
if zero:
    print(0)
elif not poss:
    print(-1)
else:
    print(steps)

    


