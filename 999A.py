n, k = map(int, input().split(' '))
ll = list(map(int, input().split(' ')))
probs = 0
while len(ll) >0:
    if ll[0] > k and ll[-1] > k:
        break
    elif ll[0] > k:
        probs+=1
        ll.pop(-1)
    elif ll[-1] > k:
        probs+=1
        ll.pop(0)
    else:
        probs+=1
        ll.pop(0)

print(probs)

