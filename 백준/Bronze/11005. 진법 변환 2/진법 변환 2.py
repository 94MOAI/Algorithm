B = []

for idx in range(10):
    B.append(idx)
for idx in range(ord('A'), ord('Z')+1):
    B.append(chr(idx))

N, target = map(int, input().split())

answer = []
while N:
    temp = N % target
    answer.insert(0, B[temp])
    N //= target

print(*answer, sep='')