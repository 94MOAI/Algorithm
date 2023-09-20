def f(depth, result):
    global answer
    if answer >= result:
        return
    elif depth  == N:
        if answer < result:
            answer = result
        return
    else:
        for idx in range(N):
            if not visited[idx]:
                visited[idx] = 1
                f(depth + 1, result * lst[depth][idx]/100)
                visited[idx] = 0


for test_case in range(1, int(input())+1):
    N = int(input())
    lst = [list(map(int, input().split())) for _ in range(N)]
    visited = [0] * N
    answer = 0
    f(0, 1)

    print(f'#{test_case}', format((answer*100), '.6f'))