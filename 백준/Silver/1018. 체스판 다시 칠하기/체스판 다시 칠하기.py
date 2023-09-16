N, M = map(int, input().split())
graph = [list(input()) for _ in range(N)]

answer = []

for i in range(N-8+1):
    for j in range(M-8+1):
        W = 0
        B = 0
        for x in range(i, i+8):
            for y in range(j, j+8):
                if (x+y)%2 == 0:
                    if graph[x][y] != 'W':
                        W += 1
                    if graph[x][y] != 'B':
                        B += 1
                else:
                    if graph[x][y] != 'B':
                        W += 1
                    if graph[x][y] != 'W':
                        B += 1
        answer.append(min(W, B))
print(min(answer))