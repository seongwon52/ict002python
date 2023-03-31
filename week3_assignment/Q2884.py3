H, M = map(int, input().split())

if H == 0 and M == 0 or H == 0 and M<45:
    H = 23
    M = M+60-45
    print(H,M)
elif M>=45 and M<=59:
    H = H
    M = M-45
    print(H,M)
else:
    H = H-1
    M = M+60-45
    print(H,M)