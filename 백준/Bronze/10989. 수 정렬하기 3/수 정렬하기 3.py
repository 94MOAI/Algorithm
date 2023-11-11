import sys
input = sys.stdin.readline

# 계수정렬
arr = [0] * (10000 + 1)
for _ in range(int(input())):
    arr[int(input())] += 1

for idx in range(len(arr)):
    if arr[idx] != 0:
        for _ in range(arr[idx]):
            print(idx)