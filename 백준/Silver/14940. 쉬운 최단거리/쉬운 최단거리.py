from collections import deque
import sys
input=sys.stdin.readline

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]

n, m = map(int, input().split())
map_arr = []
queue = deque()
visited = [[False] * m for _ in range(n)]

wall_check = [[-1] * m for _ in range(n)]

for i in range(n):
    arr = list(map(int, input().split()))

    for j in range(m):
        if arr[j] == 2:
            queue.append((i, j))
            visited[i][j] = True
            arr[j] = 0
            wall_check[i][j] = 0

        if arr[j] == 0:
            wall_check[i][j] = 0

    map_arr.append(arr)

while queue:
    x, y = queue.popleft()

    for k in range(4):
        nx = x + di[k]
        ny = y + dj[k]

        if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny]:
            if map_arr[nx][ny] == 1:
                queue.append((nx, ny))
                visited[nx][ny] = True
                wall_check[nx][ny] = wall_check[x][y] + 1

for row in wall_check:
    for i in row:
        print(i, end=' ')
    print()