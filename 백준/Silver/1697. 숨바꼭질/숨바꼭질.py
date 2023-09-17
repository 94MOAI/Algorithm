from collections import deque


def BFS():
    global dist
    while queue:
        x = queue.popleft()
        if x == K:
            return print(dist[x])
        for nx in [x-1, x+1, 2*x]:
            if 0<=nx<=100000 and not dist[nx]:
                queue.append(nx)
                dist[nx] = dist[x] + 1


queue = deque()
dist = [0]*(100000+1)
N, K = map(int, input().split())

queue.append(N)

BFS()