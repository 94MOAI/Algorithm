from itertools import combinations

import sys
input = sys.stdin.readline

mbtis = ['ISTJ', 'ISFJ', 'INFJ', 'INTJ',
         'ISTP', 'ISFP', 'INFP', 'INTP',
         'ESTP', 'ESFP', 'ENFP', 'ENTP',
         'ESTJ', 'ESFJ', 'ENFJ', 'ENTJ']

for _ in range(int(input())):
    table = {case: 0 for case in mbtis}
    n = int(input())
    test_case = input().split()
    if n > 32:
        print(0)
        continue
    else:
        for mbti in test_case:
            table[mbti] += 1
            if table[mbti] == 3:
                print(0)
                break
        else:
            test_case = list(combinations(test_case, 3))
            score_list = []
            for comb in test_case:
                score = 0
                for i in range(4):
                    if (comb[0][i] == comb[1][i] and
                            comb[0][i] == comb[2][i] and
                            comb[1][i] == comb[2][i]):
                        score += 0
                    else:
                        score += 2
                score_list.append(score)
            print(min(score_list))