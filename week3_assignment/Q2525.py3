A, B = map(int, input().split())
C = int(input())

sum = B + C
shr = sum // 60
rem = sum % 60

if shr < 1:
    A = A
    B += C
    print(A, B)
elif shr >= 1:
    if A + shr >= 24:
        A += shr - 24
    else:
        A += shr
    if rem == 0:
        B = 0
    else:
        B = rem
    print(A, B)