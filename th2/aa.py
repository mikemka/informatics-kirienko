tc = int(input()) * 60 + int(input())
tr = int(input()) * 60 + int(input())
tn = int(input()) * 60 + int(input())
tn += 24 * 60 if tn < tr else 0
tr += 24 * 60 if tr < tc else 0
tn += 24 * 60 if tn < tr else 0
t = (tn - (tnt := tc - tr + tc)) * 2
print((tnt + t) // 60 % 24, (tnt + t) % 60)
