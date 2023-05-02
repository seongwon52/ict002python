T = int(input())

sum = []

for i in range(T):
    A, B = map(int, input().split())
    sum.append(f"Case #{i+1}: {A} + {B} = {A+B}")

for i in range(len(sum)):
    print(sum[i])