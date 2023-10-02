while True:
    N = int(input())
    result = []

    if N == -1:
        break

    else:
        for number in range(1, N//2+1):
            if N % number == 0:
                result.append(number)

        if sum(result) == N:
            print(f'{N} = ', end='')
            print(' + '.join(str(i) for i in result))

        else:
            print(f'{N} is NOT perfect.')