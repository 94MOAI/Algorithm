N = int(input())

scores = list(map(int, input().split()))

M = max(scores)
for idx in range(N):
    scores[idx] = scores[idx]/M*100

average = sum(scores)/N

print(average)