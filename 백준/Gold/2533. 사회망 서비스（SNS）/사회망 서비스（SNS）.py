import sys
input = sys.stdin.readline
# 런타임 에러가 왜 뜨는건지 몰라서, 질문 참고!
sys.setrecursionlimit(10**9)

def DFS(node):
    visited[node] = True
    # 해당 노드가 얼리어답터일 경우 1, 아니라면 0
    dp[node][0], dp[node][1] = 0, 1

    for nxt_node in adj[node]:
        if not visited[nxt_node]:
            DFS(nxt_node)
            # 이전 노드가 0이라면, 다음 노드는 얼리어답터
            dp[node][0] += dp[nxt_node][1]
            # 이전 노드가 얼리어답터였다면, 다음 노드는 더 작은 수
            dp[node][1] += min(dp[nxt_node][0], dp[nxt_node][1])


N = int(input())

# 인접리스트
adj = [[] for _ in range(N+1)]

for _ in range(N-1):
    u, v = map(int, input().split())
    adj[u].append(v)
    adj[v].append(u)

# 해당 노드 포함 X or 포함 O
dp = [[0] * 2 for _ in range(N+1)]

# 노드 방문 체크
visited = [False] * (N+1)

DFS(1)

print(min(dp[1][0], dp[1][1]))