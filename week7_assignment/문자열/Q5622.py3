n = input()

lst = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
cnt = 0

for i in range(len(n)):
    for j in range(len(lst)):
        if n[i].upper() in lst[j]:
            cnt += j+3
            
print(cnt)