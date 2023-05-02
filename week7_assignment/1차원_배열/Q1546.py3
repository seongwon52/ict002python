N = int(input())
lst = list(map(int, input().split()))

a = lst[0]
M = lst[0]

for i in range(1,N,1):
    if a > lst[i]:
        a = lst[i]
    elif M < lst[i]:
        M = lst[i]

sum = 0

for i in lst:
    sum += i/M*100

print(sum/N)