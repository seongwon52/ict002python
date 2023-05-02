N = int(input())

for i in range(N):
    for j in range(i,N-1,1):
        print(" ",end='')
    for k in range(-1,i,1):
        print("*",end='')
    print()