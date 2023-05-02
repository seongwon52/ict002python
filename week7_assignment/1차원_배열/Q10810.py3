N, M = map(int, input().split())

lst = [0 for i in range(N)]

for x in range(M):
    i, j, k = map(int, input().split())
    for y in range(i-1, j):
        lst[y] = k

for j in lst:
    print(j, end=" ")