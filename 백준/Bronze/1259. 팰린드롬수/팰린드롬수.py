while True:
    N = int(input())
    if not N:
        break

    compare_N = N

    reverse_N = 0
    while N > 0:
        reverse_N *= 10
        reverse_N += N % 10
        N //= 10

    if compare_N == reverse_N:
        print('yes')
    else:
        print('no')