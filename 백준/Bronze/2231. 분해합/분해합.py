N = int(input())

for i in range(1, N+1):
    total = i

    temp = i
    # 원본변경 주의!
    while temp>0:
        total += temp%10
        temp //= 10

    if total == N:
        print(i)
        break
    if i == N:
        print(0)