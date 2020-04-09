import string
lower = list(string.ascii_lowercase)
upper = list(string.ascii_uppercase)
str1 = input().upper()
str2 = input().upper()

for i,v in zip(str1,str2):
    if i < v:
        print(-1)
        break
    elif i > v:
        print(1)
        break
else:
    print(0)



