N, M = map(int, input().split())

lst = [i for i in range(1, N+1)]

for x in range(M):
    i, j = map(int, input().split())
    a = lst[j-1]
    b = lst[i-1]
    lst[i-1] = a
    lst[j-1] = b

for y in lst:
    print(y, end=" ")