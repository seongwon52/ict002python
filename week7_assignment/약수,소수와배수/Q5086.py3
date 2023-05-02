lst = []

while True:
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        break
    elif b % a == 0:
        lst.append("factor")
    elif a % b == 0:
        lst.append("multiple")
    else:
        lst.append("neither")

for i in lst:
    print(i)