def f(depth):
    if depth == M:
        print(*subset)
        return
    check = 0
    for i in range(N):
        if used[i] or check == arr[i]:
            continue
        check = arr[i]
        subset.append(arr[i])
        used[i] = 1
        f(depth+1)
        subset.pop()
        used[i] = 0


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

used = [0] * N
subset = []

f(0)