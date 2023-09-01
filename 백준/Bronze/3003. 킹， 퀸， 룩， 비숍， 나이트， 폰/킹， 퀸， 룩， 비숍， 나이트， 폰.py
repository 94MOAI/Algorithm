# 체스는 총 16개의 피스를 사용하며, 킹 1개, 퀸 1개, 룩 2개, 비숍 2개, 나이트 2개, 폰 8개로 구성

chess = [1, 1, 2, 2, 2, 8]

donghyeuk = list(map(int, input().split()))

chess_lst_len = 0
for _ in chess:
    chess_lst_len += 1

answer = []
for idx in range(chess_lst_len):
    answer.append(chess[idx] - donghyeuk[idx])

print(*answer)