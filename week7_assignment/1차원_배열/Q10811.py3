N, M = map(int, input().split())

lst = list(i for i in range(1, N+1))

for i in range(M):
    i, j = map(int, input().split())
    lst[i-1:j] = reversed(lst[i-1:j])

for i in lst:
    print(i, end=" ")