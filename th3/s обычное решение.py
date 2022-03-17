a, b, c = int(input()), int(input()), int(input())
a2, b2, c2 = a ** 2, b ** 2, c ** 2
if a + b <= c or b + c <= a or c + a <= b:
    print('impossible')
elif a2 + b2 == c2 or b2 + c2 == a2 or c2 + a2 == b2:
    print('rectangular')
elif a2 + b2 > c2 and b2 + c2 > a2 and c2 + a2 > b2:
    print('acute')
else:
    print('obtuse')
