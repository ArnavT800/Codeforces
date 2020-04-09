n = int(input())
col = list(map(int, input().split(" ")))
col.sort()
string = ""
for i in col:
    string+=str(i)+" "
print(string)
