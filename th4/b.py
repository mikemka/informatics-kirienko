a, b = int(input()), int(input())
direction = 1
if a > b:
    direction = -1
for i in range(a, b + direction, direction):
    print(i, end=' ')
