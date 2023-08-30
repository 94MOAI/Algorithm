N, M = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(N)]
B = [list(map(int, input().split())) for _ in range(N)]
C = [[0]*M for _ in range(N)]

for y in range(N):
    for x in range(M):
        C[y][x] = A[y][x]+B[y][x]

for row in range(N):
    print(*C[row])