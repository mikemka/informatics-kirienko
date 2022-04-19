s, t = 0, 1
for i in range(1, int(input()) + 1):
    s += t + i
    t *= 2
print(s)
