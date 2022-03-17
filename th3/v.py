a, b, c, d, e = int(input()), int(input()), int(input()), int(input()), int(input())
t1 = (a <= d and b <= e or a <= e and b <= d)
t2 = (c <= d and b <= e or c <= e and b <= d)
t3 = (a <= d and c <= e or a <= e and c <= d)
if t1 or t2 or t3:
    print('YES')
else:
    print('NO')
