# 유니온 파인드
import sys
input = sys.stdin.readline

def make_set(N):
    return [i for i in range(N+1)]

def find_set(A, x):
    if A[x] == x:
        return x
    else:
        A[x] = find_set(A, A[x])
        return A[x]

def union(A, x, y):
    px = find_set(A, x)
    py = find_set(A, y)

    if px != py:
        A[px] = py
        return A

# n : 집합의 개수 + 1, m : 그 후의 연산
N, M = map(int, input().split())

# 집합 초기화 (make_set)
parents = make_set(N)

# 연산 갯수 M개 만큼 입력 받아서 처리
for _ in range(M):
    oper, a, b = map(int, input().split())
    # 집합을 합치는 연산 '0'
    if not oper:
        union(parents, a, b)
    # 집합이 서로 같은지 확인하는 연산 '1'
    elif oper:
        if a == b:
            print('YES')
        elif find_set(parents, a) == find_set(parents, b):
            print('YES')
        else:
            print('NO')
