a, b = int(input()), int(input())
k = 0
while a >= b:
    a -= b
    k += 1
print(k, a)
