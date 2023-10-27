N, K = map(int, input().split())

idx = 0
queue = [i for i in range(1, N+1)]
answer = []
while queue:
    idx += K-1
    if idx >= len(queue):
        idx %= len(queue)
    answer.append(queue.pop(idx))

print("<" + ", ".join(map(str, answer)) + ">")