import sys
input = sys.stdin.readline
from collections import deque

def BFS(node, result):
    q = deque()
    q.append(node)
    visited = [False] * (N + 1)
    visited[node] = True
    result += 1
    while q:
        node = q.popleft()
        for i in lst[node]:
            if visited[i]:
                continue
            else:
                q.append(i)
                visited[i] = True
                result += 1

    return result


N, M = map(int, input().split())
lst = [[] for _ in range(N + 1)]
computer = []
infected = 0

for i in range(M):
    A, B = map(int, input().split())
    lst[B].append(A)

for node in range(1, N + 1):
    temp = BFS(node, 0)
    if infected < temp:
        computer = []
        infected = temp
        computer.append(node)
    elif infected == temp:
        computer.append(node)

print(*sorted(computer))