def make(N):
    return [parent for parent in range(N+1)]


def find(parent, x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent, parent[x])
        return parent[x]


def union(parent, x, y):
    px = find(parent, x)
    py = find(parent, y)

    if px == py:
        # print('Cycle')
        return

    if px < py:
        parent[py] = px
    else:
        parent[px] = py


for test_case in range(int(input())):
    # N : 창용마을 사람의 수
    # M : 서로 알고 있는 사람의 관계 수 (양방향)
    N, M = map(int, input().split())

    relation = make(N)
    for _ in range(M):
        s, e = map(int, input().split())
        union(relation, s, e)

    answer = set()
    for idx in range(1, N+1):
        answer.add(find(relation, idx))

    print(f'#{test_case + 1} {len(answer)}')