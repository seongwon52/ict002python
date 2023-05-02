s = input()

alpha = 'abcdefghijklmnopqrstuvwxyz'

result = [-1] * len(alpha)

for ch in s:
    if ch in alpha:
        result[alpha.index(ch)] = s.index(ch)

for r in result:
    print(r, end=" ")