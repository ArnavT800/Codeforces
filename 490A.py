n = int(input())
c = list(map(int, input().split(" ")))
lst = []
one = c.count(1)
two = c.count(2)
three = n- (one+two)
lst.append(one)
lst.append(two)
lst.append(three)
print(min(lst))
