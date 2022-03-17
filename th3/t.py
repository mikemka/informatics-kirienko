n = int(input())
a, b, c = n // 60, n % 60 // 10, n % 10
if c * 15 > 125:
    c = 0
    b += 1
if c * 15 + b * 125 > 440:
    c = 0
    b = 0
    a += 1
print(c, b, a)
