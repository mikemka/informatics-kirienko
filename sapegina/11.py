b = int(input())
v, t = 1, 0
while b > 0:
    b -= v
    b *= 2
    v *= 2
    t += 1
print(t)
