import sys
lst = [int(sys.stdin.readline()) for i in range(10)]

r = []

for i in range(len(lst)):
    r.append(lst[i] % 42)
    
cnt = list(0 for i in range(10))

for i in range(len(r)):
    for j in range(len(r)):
        if r[i] == r[j] and i != j:
            r[i] = -1

tot = 0

for i in r:
    if i != -1:
        tot += 1
print(tot)