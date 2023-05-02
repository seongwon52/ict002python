N, X = map(int, input().split())

lst = list(map(int, input().split()))

cnt = []

for i in lst:
    if i < X:
        cnt.append(i)

for i in cnt:
    print(i, end=' ')