n = int(input())
finalList = []
for i in range(n):
    countList = 0
    stud = int(input())
    ap = input()
    a = False
    count = 0
    for k in range(stud):
        if ap[k] == "A" and not a:
            a = True
            count = 0
        elif ap[k] =="P" and a:
            count+=1
            if count>countList:
                countList = count
        elif ap[k] == "A" and a:
            count = 0
            
    finalList.append(countList)


finalList = map(str, finalList)
for i in finalList:
    print(*i)



        
        


