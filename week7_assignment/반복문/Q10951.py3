sum = []

while True:
    try:
        A, B = map(int, input().split())
        sum.append(A+B)
    except:
        break

for i in sum:
    print(i)