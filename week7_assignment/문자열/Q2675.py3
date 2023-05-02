T = int(input())

lst = []
A = ""

for i in range(T):
    R, S = map(str, input().split())
    for j in range(len(S)):
        if j == 0:
            A = ""
        A += S[j] * int(R)
        if j == len(S)-1:
            lst.append(A)

for i in lst:
    print(i)