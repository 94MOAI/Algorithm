# import sys
# input = sys.stdin.readline


def BFS(current_node):
    global answer
    queue = []
    queue.append(current_node)
    visited[current_node] = 1
    while queue:
        node = queue.pop(0)
        # if not graph[node]:
        #     answer.append(node)
        # print(node, end=" ")
        for nxt in graph[node]:
            if not visited[nxt]:
                queue.append(nxt)
                visited[nxt] = visited[node] + 1


for test_case in range(1, 10+1):
    N, S = map(int, input().split())
    edges = list(map(int, input().split()))

    graph = [[] for _ in range(100+1)]

    for idx in range(0, len(edges), 2):
        u = edges[idx]
        v = edges[idx+1]
        graph[u].append(v)
    # print(graph)
    visited = [0] * (100 + 1)

    BFS(S)

    depth = max(visited)
    answer = []
    for idx in range(100+1):
        if depth == visited[idx]:
            answer.append(idx)

    answer.sort()

    print(f'#{test_case} {answer[-1]}')
