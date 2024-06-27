import random

B = int(random.randint(1,20))
A = int(random.randint(1,B))
arr = []
while A <= B:
    if A%2 == 0:
       arr.append(A)
    A += 1
for i in arr:
    print(i, ' ', end='')
    i += 1
print(" ")