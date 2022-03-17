e = int(input())
if 11 <= e <= 19:
    print(f'{e} korov')
else:
    if e % 10 == 1:
        print(f'{e} korova')
    elif e % 10 in (2, 3, 4):
        print(f'{e} korovy')
    else:
        print(f'{e} korov')
