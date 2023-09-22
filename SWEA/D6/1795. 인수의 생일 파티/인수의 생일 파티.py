'''
test case
s, e, dist

1
4 8 2
1 2 4
1 3 2
1 4 7
2 1 1
2 3 5
3 1 2
3 4 4
4 2 3
'''
import heapq

def dijkstra(graph, start):
    time = [float('inf')] * (N+1)
    time[start] = 0
    mn_heap = [(0, start)]

    while mn_heap:
        now, node = heapq.heappop(mn_heap)

        if now > time[node]:
            continue

        for nxt, extra in graph[node]:
            nxt_time = now + extra
            if time[nxt] > nxt_time:
                time[nxt] = nxt_time
                heapq.heappush(mn_heap, (nxt_time, nxt))

    return time


for test_case in range(int(input())):
    # N : 집 (1~N), M : 연결 관계 갯수, X : 인수의 집(도착지)
    N, M, X = map(int, input().split())

    forward = [[] for _ in range(N+1)]
    reverse = [[] for _ in range(N+1)]
    for _ in range(M):
        # x, y, c = 출발노드, 도착노드, 걸리는 시간
        x, y, c = map(int, input().split())
        forward[x].append((y, c))
        reverse[y].append((x, c))

    forward_time = dijkstra(forward, X)
    reverse_time = dijkstra(reverse, X)

    # print(forward_time)
    # print(reverse_time)

    answer = 0
    for idx in range(1, N+1):
        total_time = forward_time[idx] + reverse_time[idx]
        if answer < total_time:
            answer = total_time

    print(f'#{test_case+1} {answer}')