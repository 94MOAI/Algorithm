def f(text, y, x):
    global answer

    if len(text) == 7:
        answer.add(text)
        return

    for dy, dx in [(0, -1), (-1, 0), (0, 1), (1, 0)]:
        ny = y + dy
        nx = x + dx
        if 0 <= ny < 4 and 0 <= nx < 4:
            f(text + graph[ny][nx], ny, nx)


for test_case in range(int(input())):
    graph = [input().split() for _ in range(4)]

    answer = set()
    for y in range(4):
        for x in range(4):
            f('', y, x)

    print(f'#{test_case+1} {len(answer)}')