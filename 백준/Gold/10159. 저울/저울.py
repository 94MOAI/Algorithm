N = int(input())
M = int(input())

# 대소비교 초기화
weight = [[float('inf')] * (N + 1) for _ in range(N + 1)]

for self in range(1, N + 1):
    weight[self][self] = 1


# 왼쪽이 오른쪽에 비해 더 무겁다!
for _ in range(M):
    heavy, light = map(int, input().split())
    weight[heavy][light] = 1
    weight[light][heavy] = -1

for all in range(1, N + 1):
    for heavy in range(1, N + 1):
        for light in range(1, N + 1):
            # if weight[heavy][light] > weight[heavy][all] + weight[all][light]:
            #     weight[heavy][light] = weight[heavy][all] + weight[all][light]
            if weight[heavy][all] == weight[all][light] != float('inf'):
                weight[heavy][light] = weight[heavy][all]


for heavy in range(1, N + 1):
    result = 0
    for light in range(1, N + 1):
        if weight[heavy][light] == float('inf'):
            result += 1
    print(result)