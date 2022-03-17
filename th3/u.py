n = int(input())
k = n // 60
n = n % 60
if n < 5:
    print (n, 0, 0, 0, k)
elif 5 <= n <= 8:
    print (n - 5, 1, 0, 0, k)
elif 9 <= n <= 10:
    print (0, 0, 1, 0, k)
elif 11 <= n <= 14:
    print (n - 10, 0, 1, 0, k)
elif 15 <= n <= 17:
    print (n - 15, 1, 1, 0, k)
elif 18 <= n <= 20:
    print (0, 0, 0, 1, k)
elif 21 <= n <= 24:
    print (n - 20, 0, 0, 1, k)
elif 25 <= n <= 28:
    print (n - 25, 1, 0, 1, k)
elif 29 <= n <= 30:
    print (0, 0, 1, 1, k)
elif 31 <= n <= 34:
    print (n - 30, 0, 1, 1, k)
elif n == 35:
    print (0, 1, 1, 1, k)
elif 36 <= n <= 60:
    print (0, 0, 0, 0, k + 1)
