import sys
from collections import deque

input = sys.stdin.readline

def bfs():
    global q
    while q:
        y, x = q.popleft()
        for dy, dx in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
            nx = x + dx
            ny = y + dy
            if 0<=nx< m and 0<=ny<n and box[ny][nx] == 0:
                q.append((ny, nx))
                box[ny][nx] = box[y][x] + 1


m, n = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(n)]

q = deque()

for y in range(n):
    for x in range(m):
        if box[y][x] == 1:
            q.append((y, x))

bfs()

day = 0
for y in range(n):
    if 0 in box[y]:
        day = 0
        break
    for x in range(m):
        if day < box[y][x]:
            day = box[y][x]

print(day - 1)