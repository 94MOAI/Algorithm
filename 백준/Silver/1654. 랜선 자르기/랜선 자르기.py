def binarySearch(A:list):
    s = 1
    e = A[-1]

    while s <= e:

        mid = (s + e) // 2
        cnt = 0

        for i in LAN:
            cnt += i // mid

        if cnt < N:
            e = mid - 1

        if cnt >= N:
            s = mid + 1

    return e


K, N = map(int, input().split())

LAN = [int(input()) for _ in range(K)]

# 이분탐색은 반드시 정렬된 상태여야 한다.
LAN.sort()

answer = binarySearch(LAN)

print(answer)
