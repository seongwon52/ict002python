a, b, c = map(int, input().split())

if a == b == c:
    print(10000 + (a or b or c) * 1000)
elif a == b or b == c or a == c and not a == b == c:
    if a == b and a != c:
        print(1000 + (a or b) * 100)
    elif b == c and b != a:
        print(1000 + (b or c) * 100)
    elif c == a and c != b:
        print(1000 + (c or a) * 100)
else:
    max = a if a > b else b
    max = c if c > max else max
    print(max * 100)