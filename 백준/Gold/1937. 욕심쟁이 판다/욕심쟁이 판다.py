import sys
sys.setrecursionlimit(10 ** 6)

delta = ((0, -1), (-1, 0), (0, 1), (1, 0))

def f(y, x):
    if dp[y][x]:
        # 이미 대나무 쿰척했으면 그대로 반환
        return dp[y][x]

    else:
        # 아직 안간곳이니까 방문 체크
        dp[y][x] = 1
        # 사방탐색
        for dy, dx in delta:
            ny, nx = y + dy, x + dx
            if 0 <= ny < N and 0 <= nx < N:
                # 대나무 많아? 이동하셈
                if maps[ny][nx] > maps[y][x]:
                    # 그 칸에 이미 있던 이동거리하고, 내 이동거리 +1 하고 비교
                    dp[y][x] = max(dp[y][x], f(ny, nx) + 1)

        return dp[y][x]


N = int(input())
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]

answer = 0
for y in range(N):
    for x in range(N):
        if dp[y][x] == 0:
            answer = max(f(y, x), answer)

print(answer)