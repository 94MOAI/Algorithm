for _ in range(int(input())):
    H, W, N = map(int, input().split())

    if not N%H:
        X = str(N//H)
        Y = str(H)
    else:
        X = str(N//H+1)
        Y = str(N%H)

    if len(X) == 1:
        X = '0'+X

    print(Y+X)
