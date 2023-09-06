
# 9 X 9 행렬
lst = [list(map(int, input().split())) for _ in range(9)]

# 2차원 배열 탐색
# 문제의 조건 : 주어지는 수 0~99
mx = 0
# 주의사항! : 인덱스는 0 번이지만, 출력은 1번부터 시작!
x_idx = y_idx = 1
for i in range(9):
    for j in range(9):
        if mx < lst[i][j]:
            mx = lst[i][j]
            # 인덱스는 0번 -> 출력은 1 부터
            x_idx, y_idx = i+1, j+1

print(mx)
print(x_idx, y_idx)