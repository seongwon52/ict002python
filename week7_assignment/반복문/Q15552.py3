import sys

T = int(input())

sum = []

for i in range(T):
    A, B = map(int, sys.stdin.readline().split())
    sum.append(A+B)

for i in range(len(sum)):
    print(sum[i])