n = input().strip()

if not n:
    print(0)
else:
    cnt = 1
    for i in range(len(n)):
        if i == len(n)-1 and n[i] == " ":
            cnt -= 1
        elif i == 0 and n[i] == " ":
            cnt -= 1  
        elif ord(n[i]) == 32: 
            cnt += 1
    print(cnt)