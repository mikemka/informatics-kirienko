# Решение на min(), max()

n, m, x, y = int(input()), int(input()), int(input()), int(input())
print(min(x, y, abs(min(n, m) - x), abs(max(n, m) - y)))
