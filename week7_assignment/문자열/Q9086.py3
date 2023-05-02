T = int(input())

lst = []

for i in range(T):
    n = input()
    lst.append(n[0]+n[-1])

for j in lst:
    print(j)