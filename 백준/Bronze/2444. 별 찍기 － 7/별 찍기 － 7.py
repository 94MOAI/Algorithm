N = int(input())

for idx in range(1, 2*N):
    if idx <= N:
        print(' ' * (N-idx), end='')
        print('*' * (2*idx-1))
    else:
        print(' ' * (idx-N), end='')
        print('*' * (2*(2*N-idx)-1))
