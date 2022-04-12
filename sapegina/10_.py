a, b, n = int(input()), int(input()), int(input())
for i in range(1, n + 1):
    a *= 1.05
    a -= b
    print(i, a)
