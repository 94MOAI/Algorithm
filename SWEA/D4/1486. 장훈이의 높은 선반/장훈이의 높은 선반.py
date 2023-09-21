def subset(n, bit, total):
    global mn
    if total >= B:
        if mn > total:
            mn = total
        return

    if n == bit:
        return
    else:
        checked[bit] = 1
        subset(n, bit + 1, total + tall[bit])
        checked[bit] = 0
        subset(n, bit + 1, total)
        
for test_case in range(1, int(input()) + 1):
    N, B = map(int, input().split())
    tall = list(map(int, input().split()))
    
    checked = [0] * N
    mn = 10000 * N
    
    subset(N, 0, 0)
    print(f'#{test_case} {mn - B}')