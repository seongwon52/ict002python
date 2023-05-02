T = int(input())

sum = []

for i in range (T):
    A, B = map(int, input().split())
    sum.append(A+B)

for j in range(len(sum)):
    print(sum[j])