def f(depth):
    if depth == M:
        print(*subset)
        return
    for i in range(N):
        subset.append(arr[i])
        f(depth+1)
        subset.pop()


N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()

used = [0] * N
subset = []

f(0)