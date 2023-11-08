from collections import deque
import sys

input = sys.stdin.readline

def bfs(start):
    queue = deque()
    queue.append(start)

    visited[start] = True

    while queue:
        cp = queue.popleft()

        for d in range(1, 6+1):
            np = cp + d

            if 0 < np <= 100 and not visited[np]:
                if np in snake:
                    np = snake[np]

                if np in ladder:
                    np = ladder[np]

                if not visited[np]:
                    queue.append(np)
                    visited[np] = 1
                    board[np] = board[cp] + 1


N, M = map(int, input().split())

board = [0 for idx in range (100+1)]
visited = [0 for idx in range(100+1)]

ladder = dict()
for _ in range(N):
    x, y = map(int,input().split())
    ladder[x] = y

snake = dict()
for _ in range(M):
    u, v = map(int,input().split())
    snake[u] = v


bfs(1)
print(board[100])