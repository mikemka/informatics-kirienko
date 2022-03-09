n, k, m = int(input()), int(input()), int(input())
print((y := int((((x := k - k % m) + (x ** 2) ** 0.5) // 2) / (x + 1) + 0.5)) * ((n - k % m) // (x + int(((y - 1) ** 2) ** 0.5))) * (x // m))
