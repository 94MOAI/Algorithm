# EOFError에서 EOF 는 END OF FILE 즉 문자의 끝을 의미합
# 사용자가 입력을 마칠 경우 이 EOF가 인식되며 EOFError 는 EOF가 입력될 경우 나타나는 에러

# while True:
#     try:
#         print(input())
#     except EOFError:
#         break

# input()은 EOF를 받을 때 EOFError를 일으키지만
# sys.stdin.readline은 EOF를 받을 때 빈 문자열을 리턴

import sys

while True:
    text = sys.stdin.readline().rstrip()

    if text == '':
        break
    else:
        print(text)