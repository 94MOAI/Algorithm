import sys
from collections import deque

delta = [(0, -1), (-1, 0), (0, 1), (1, 0)]
input = sys.stdin.readline

def bfs(x, y):
    visited = [[0] * N for _ in range(N)]
    queue = deque([[x, y]])
    state = []

    visited[x][y] = 1

    while queue:
        i, j = queue.popleft()

        for dx, dy in delta:
            ni, nj = i + dx, j + dy
            if 0 <= ni < N and 0 <= nj < N and visited[ni][nj] == 0:
                if area[x][y] > area[ni][nj] and area[ni][nj] != 0:
                    visited[ni][nj] = visited[i][j] + 1
                    state.append((visited[ni][nj] - 1, ni, nj))
                elif area[x][y] == area[ni][nj]:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append([ni, nj])
                elif area[ni][nj] == 0:
                    visited[ni][nj] = visited[i][j] + 1
                    queue.append([ni, nj])

    # return state.sort(key=lambda x: (x[0], x[1], x[2]))
    return sorted(state, key=lambda x: (x[0], x[1], x[2]))


N = int(input())
area = [list(map(int, input().split())) for _ in range(N)]

baby_shark = []
for i in range(N):
    for j in range(N):
        if area[i][j] == 9:
            baby_shark.append((i, j))

answer = 0

i, j = baby_shark[0]
size = [2, 0]
while True:
    area[i][j] = size[0]
    state = deque(bfs(i, j))

    if not state:
        break

    step, nx, ny = state.popleft()
    answer += step
    size[1] += 1

    if size[0] == size[1]:
        size[0] += 1
        size[1] = 0

    area[i][j] = 0
    i, j = nx, ny

print(answer)