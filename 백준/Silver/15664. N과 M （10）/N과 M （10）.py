def f(depth, index):
    if depth == M:
        print(*subset)
        return
    memo = 0
    for i in range(index, N):
        if used[i] or memo == arr[i]:
            continue
        memo = arr[i]
        used[i] = 1
        subset.append(arr[i])
        f(depth+1, i+1)
        used[i] = 0
        subset.pop()



N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
used = [0]*N
subset = []

f(0, 0)