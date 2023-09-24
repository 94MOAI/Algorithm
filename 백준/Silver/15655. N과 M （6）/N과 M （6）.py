def f(depth, index):
    if depth == M:
        print(*subset)
        return
    for i in range(index, N):
        if used[i]:
            continue
        subset.append(arr[i])
        used[i] = 1
        f(depth+1, i+1)
        subset.pop()
        used[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

used = [0] * N
subset = []
f(0, 0)