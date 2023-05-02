import sys
lst = [int(sys.stdin.readline()) for i in range(28)]

num_lst = list(range(1,31))

for i in lst:
    for j in num_lst:
        if i == j:
            num_lst.remove(j)

for k in num_lst:
    print(k)