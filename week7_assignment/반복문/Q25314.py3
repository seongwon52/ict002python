N = int(input())

x = N//4

for i in range(x):
    print("long ", end="")
    if i == x-1:
        print("int")