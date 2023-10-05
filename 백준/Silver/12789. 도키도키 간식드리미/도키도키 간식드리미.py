# def bubble_sort(lst, len_lst):
#     sort_list = lst[:]
#
#     for i in range(len_lst):
#         for j in range(0, len_lst-i-1):
#             if sort_list[j] > sort_list[j+1]:
#                 sort_list[j], sort_list[j+1] = sort_list[j+1], sort_list[j]
#     return sort_list
#
#
# N = int(input())
#
# line = list(map(int, input().split()))
#
# sort_lst = bubble_sort(line, N)
#
# stack = []
#
# while True:
#     for i in range(N):
#         if line[i] != sort_lst[0]:
#             stack.append(line[i])
#         else:
#             sort_lst.pop(0)
#
#     for _ in range(len(stack)):
#         if stack[-1] == sort_lst[0]:
#             stack.pop()
#             sort_lst.pop(0)
#         else:
#             break
#
#     # print(stack)
#
#     if len(stack) == 0:
#         print('Nice')
#         break
#     else:
#         print('Sad')
#         break

# **************************************************

# N = int(input())
# num = list(map(int, input().split()))
# stack = [] # 웨이팅 존
# order = 1 # 간식 받을 순서
#
# for i in num:
#     stack.append(i)
#
# # 스택의 마지막 값이 순서랑 같으면 삭제
#
# for k in stack:
#     if stack[-1] == order:
#         stack.pop(-1)
#         # 간식 받으면 다음 사람 순번 올려주기
#         order += 1
#
# # print(stack)
#
# # 스택의 마지막이 앞에것들보다 크면 안된다
# result = ''
# for j in stack:
#     # 다 삭제해서 스택에 값이 없으면 nice
#     if len(stack) == 0:
#         result = 'Nice'
#         break
#     if len(stack) > 1:
#         if stack[-1] > stack[-2]:
#             result = 'Sad'
#         else:
#             result = 'Nice'
#
# print(result)

# **************************************************


# 12789. 도키도키 간식드리미
# 숭환이가 무사히 간식을 받을 수 있으면 "Nice" 없으면 "Sad"

N = int(input())
lst = list(map(int, input().split()))
stack = []  # 웨이팅 존
order = 1   # 간식 받을 순서

# 입력 받은 동안
while lst:
    if lst[0] == order:
        lst.pop(0)
        order += 1
    else:
        stack.append(lst.pop(0))
    # 순서가 맞지 않으면 웨이팅 존으로 들어간다.

    while stack:
        # 스택의 최상단이 순서에 맞다면, 간식 받기
        if stack[-1] == order:
            stack.pop()
            order += 1
        else: # 순서가 맞지 않다면 승환이 간식 못받아~
            break

# 실행이 다 끝났을 떄 스택에 안무것도 안 남아있으면 Nice
if stack:
    print('Sad')
else:
    print('Nice')
