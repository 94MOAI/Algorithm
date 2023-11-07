# 1 2 3 4 5 6 7 8 9
#
#   2   2   2   2 3
#           3   4
#

N = int(input())

res = 0
for i in range(2, int(N ** 0.5) + 1):
    j = N // i
    res += (j + i) * (j - i + 1) // 2
    res += (j - i) * i

res %= 1000000
print(res)