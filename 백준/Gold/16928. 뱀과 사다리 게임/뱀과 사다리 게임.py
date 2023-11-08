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
                if np in move:
                    visited[np] = 1
                    np = move[np]

                if not visited[np]:
                    queue.append(np)
                    visited[np] = 1
                    board[np] = board[cp] + 1



N, M = map(int, input().split())

board = [0 for idx in range (100+1)]
visited = [0 for idx in range(100+1)]

move = dict()

for _ in range(N+M):
    x, y = map(int, input().split())
    move[x] = y

bfs(1)
print(board[100])