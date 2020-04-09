n, k = list(map(int, input().split(" ")))
count = 0
passw = ""
alph = ['a', 'b', 'c', 'd' ,'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n' ,'o', 'p','q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
while count<n:
    if len(passw) == k:
        
    passw+=alph[0]
    alph.pop(0)
    count+=1
print(passw)

