def BFS(node):
    queue = []
    queue.append(node)

    contact[node] = 1

    while queue:
        now = queue.pop(0)

        for nxt in adj[now]:
            if contact[nxt]:
                continue
            queue.append(nxt)
            contact[nxt] = contact[now] + 1


for test_case in range(1, 10+1):
    N, S = map(int, input().split())
    adj_arr = list(map(int, input().split()))

    adj = [[] for _ in range(100+1)]
    for idx in range(0, N, 2):
        s = adj_arr[idx]
        e = adj_arr[idx + 1]
        adj[s].append(e)

    contact = [0] * (100 + 1)
    BFS(S)

    mx_contact = 0
    for idx in range(100+1):
        if mx_contact < contact[idx]:
            mx_contact = contact[idx]

    mx_node = 0
    for idx in range(100+1):
        if contact[idx] == mx_contact and mx_node <= idx:
            mx_node = idx

    print(f'#{test_case} {mx_node}')