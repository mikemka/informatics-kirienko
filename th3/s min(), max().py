a1, b1, c1 = int(input()), int(input()), int(input())
c = max(a1, b1, c1)
b = min(a1, b1, c1)
a = a1 + b1 + c1 - b - c
if c >= a + b:
    print('impossible')
elif c ** 2 == a ** 2 + b ** 2:
    print('rectangular')
elif c ** 2 < a ** 2 + b ** 2:
    print('acute')
elif c ** 2 > a ** 2 + b ** 2:
    print('obtuse')
