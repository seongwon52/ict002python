first = int(input())
second = int(input())

num = [int(a) for a in str(second)]

third = first * num[2]
fourth = first * num[1]
fifth = first * num[0]

fi = int(str(fifth)+"00")
fo = int(str(fourth)+"0")

sum = third + fi + fo

print(third)
print(fourth)
print(fifth)
print(sum)