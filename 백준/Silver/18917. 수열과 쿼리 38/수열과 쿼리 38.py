import sys

input = sys.stdin.readline

M = int(input())
total = 0
xor = 0

for _ in range(M):
    arr = list(map(int, input().split()))
    if arr[0] == 1:
        total += arr[1]
        xor ^= arr[1]
    elif arr[0] == 2:
        total -= arr[1]
        xor ^= arr[1]
    elif arr[0] == 3:
        print(total)
    else:
        print(xor)