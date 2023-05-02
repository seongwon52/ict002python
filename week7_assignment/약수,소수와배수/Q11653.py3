N = int(input())

div = []

if N == 2:
    div.append(2)
else:
    for i in range(2, N):
        if N % i == 0:
            while N % i == 0:
                N //= i
                div.append(i)

    if N > 2:
        div.append(N)

for i in div:
    print(i)