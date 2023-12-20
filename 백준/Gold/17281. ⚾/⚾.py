import sys
from itertools import permutations
input = sys.stdin.readline

N = int(input())
innings = []
for _ in range(N):
    innings.append(list(map(int, input().split())))

temp = [1, 2, 3, 4, 5, 6, 7, 8]

answer = 0

for case in permutations(temp):
    test_order = list(case)
    play_order = test_order[:3] + [0] + test_order[3:]
    score = 0
    current_player = 0

    for inning in range(N):
        out_cnt = 0
        first, second, third = 0, 0, 0

        while out_cnt < 3:
            result = innings[inning][play_order[current_player]]
            if result == 0:
                out_cnt += 1
            elif result == 1:
                score += third
                first, second, third = 1, first, second
            elif result == 2:
                score += second + third
                first, second, third = 0, 1, first
            elif result == 3:
                score += first + second + third
                first, second, third = 0, 0, 1
            else:
                score += first + second + third + 1
                first, second, third = 0, 0, 0
                
            current_player = (current_player + 1) % 9

    if answer <= score:
        answer = score

print(answer)