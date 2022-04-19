c1, z1, c2, z2 = int(input()), int(input()), int(input()), int(input())
c, z = c3, z3 = c1 * z2 + c2 * z1, z1 * z2
while c3 != 0 and z3 != 0:
    if c3 > z3:
        c3 %= z3
    else:
        z3 %= c3
print(f'{c // (z3 + c3)}/{z // (z3 + c3)}')
