# import sys
# input = sys.stdin.readline
# 
# N = int(input())
# sangguen = list(map(int, input().split()))
# M = int(int(input()))
# cards = list(map(int, input().split()))
# 
# d = {}
# for card in cards:
#     d[card] = 0
# 
# for card in sangguen:
#     if card in list(d.keys()):
#         d[card] += 1
# 
# 
# print(*list(d.values()))


import sys
input = sys.stdin.readline

N = int(input())
cards = [*map(int, input().split())]
M = int(input())
candidate = [*map(int, input().split())]

count = {}
for card in cards:
    if card in count:
        count[card] += 1
    else:
        count[card] = 1

for target in candidate:
    result = count.get(target)
    if result == None:
        print(0, end=" ")
    else:
        print(result, end=" ")