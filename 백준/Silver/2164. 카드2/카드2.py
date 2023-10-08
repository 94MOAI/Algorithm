# def solve(lst):
#     while len(lst) > 1:
#         lst.pop(0)
#         lst.append(lst.pop(0))
#     return lst
#
#
# N = int(input())
#
# queue = [i for i in range(1, N+1)]
#
# print(*solve(queue))

from collections import deque

N = int(input())
deque = deque([i for i in range(1, N + 1)])

while (len(deque) > 1):
    deque.popleft()
    move_num = deque.popleft()
    deque.append(move_num)

print(deque[0])