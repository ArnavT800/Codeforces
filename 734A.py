n = int(input())
g = input()
a = g.count("A")
d = n-a
if a>d:
    print("Anton")
elif a<d:
    print("Danik")
else:
    print("Friendship")
    