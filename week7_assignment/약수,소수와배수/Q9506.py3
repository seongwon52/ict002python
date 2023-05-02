while True:
    num = int(input())
    if num == -1:
        break
    lst = list(range(1, num))
    tot = 0
    x = []

    for i in range(0, len(lst)):
        if num % lst[i] == 0:
            tot += lst[i]
            x.append(str(lst[i]))

    if tot == num:
        print(f"{num} = {' + '.join(x)}")
    else:
        print(f"{num} is NOT perfect.")