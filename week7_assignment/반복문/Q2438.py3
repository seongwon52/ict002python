N = int(input())

for i in range(N,0,-1):
    for j in range(N+1,i,-1):
        print("*",end='')
    print()