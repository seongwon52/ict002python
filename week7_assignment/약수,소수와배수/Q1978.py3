N = int(input())
lst = list(map(int, input().split()))

cnt_p = 0

for i in lst:
    num = list(range(2, i+1))
    cnt = 0
   
    for j in num:
        if i % j == 0:
            cnt += 1
    if cnt == 1:
        cnt_p += 1

print(cnt_p)