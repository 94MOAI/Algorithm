N, M = map(int, input().split())

A = [0]*N

for _ in range(M):
    s, e, ball = map(int, input().split())
    for idx in range(s-1, e):
        A[idx] = ball

print(*A)