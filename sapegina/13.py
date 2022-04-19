from random import randint

x, s = randint(1, 50), 1
e = int(input())
while e != x:
    if x > e:
        print('Больше!')
    elif x < e:
        print('Меньше!')
    s += 1
    e = int(input())
print(f'Вы отгадали с {s} попытки!')
