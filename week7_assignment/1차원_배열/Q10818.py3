N = int(input())

lst = list(map(int, input().split()))

A = lst[0]
B = lst[0]

for i in range(1,len(lst),1):
    if A > lst[i]:
        A = lst[i]
    elif B < lst[i]:
        B = lst[i]

print(A, B)