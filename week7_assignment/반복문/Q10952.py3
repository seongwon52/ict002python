sum = []

while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break
    sum.append(A+B)
    
for i in sum:
    print(i)