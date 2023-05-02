M = int(input())
N = int(input())

lst = list(range(M, N+1))
if 1 in lst:
    lst.remove(1)

for i in range(M, N+1):
    for j in range(2, i):
        if i % j == 0:
            lst.remove(i)
            break

if len(lst) == 0:
    print("-1")
else:
    print(sum(lst))
    print(min(lst))