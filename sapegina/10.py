a, b, c = int(input()), int(input()), int(input())
k = 0
while a >= c:
    a *= 1.05
    a -= b
    k += 1
print(k)
