import sys
input = sys.stdin.readline

N = int(input())

adj = []
for _ in range(N):
    adj.append([int(x) for x in input().rstrip().split()])

for k in range(N):
    for i in range(N):
        for j in range(N):
            if adj[i][k] == 1 and adj[k][j] == 1:
                adj[i][j] = 1

for row in adj:
    print(' '.join(map(str, row)))