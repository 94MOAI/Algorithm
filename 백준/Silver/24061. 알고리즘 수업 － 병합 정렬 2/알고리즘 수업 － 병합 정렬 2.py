
def merge_sort(A, p, r):
    if p < r:
        q = (p + r) // 2 # q는 p, r의 중간 지점
        merge_sort(A, p, q)  # 전반부 정렬
        merge_sort(A, q + 1, r) # 후반부 정렬
        merge(A, p, q, r) # 병합


def merge(A, p, q, r):
    global count
    i, j = p, q + 1
    tmp = []

    while i <= q and j <= r:
        if (A[i] <= A[j]):
            tmp.append(A[i])
            res.append(A[i])
            i += 1
        else:
            tmp.append(A[j])
            res.append(A[i])
            j += 1

    while i <= q:
        tmp.append(A[i])
        res.append(A[i])
        i += 1

    while j <= r:
        tmp.append(A[j])
        res.append(A[i])
        j += 1

    i, t = p, 0

    while i <= r:
        A[i] = tmp[t]
        count += 1
        if count == K:
            print(*A)
            quit()
        i += 1
        t += 1

N, K = map(int, input().split())
A = list(map(int, input().split()))
count = 0
res = []

merge_sort(A, 0, N - 1)

if len(res) < K:
    print(-1)