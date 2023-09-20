import sys
input = sys.stdin.readline

def find(x):
    if parent[x] == x:
        return x
    else:
        parent[x] = find(parent[x])
        return parent[x]

def union(x, y):
    px = find(x)
    py = find(y)

    if px != py:
        parent[py]  = px
        answer[px] += answer[py]

# 입력
for _ in range(int(input())):
    relation = int(input())
    # 로직
    parent = dict()
    answer = dict()
    for _ in range(relation):
        x, y = input().split()
        # 초기 집합이 만들어 지지 않은 상태일 때!
        if x not in parent:
            parent[x] = x
            answer[x] = 1
        if y not in parent:
            parent[y] = y
            answer[y] = 1

        # 출력
        union(x, y)
        print(answer[find(x)])