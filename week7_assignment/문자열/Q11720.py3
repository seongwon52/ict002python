N = int(input())

num = int(input())
x = str(num)

sum = 0

for i in range(len(x)):
    sum += int(x[i])

print(sum)