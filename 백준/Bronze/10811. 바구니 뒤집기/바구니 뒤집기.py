N, M = map(int, input().split())

basket = [i for i in range(1, N+1)]

for _ in range(M):
    s, e = map(int, input().split())
    basket[s-1:e] = basket[s-1:e][::-1]

print(*basket)