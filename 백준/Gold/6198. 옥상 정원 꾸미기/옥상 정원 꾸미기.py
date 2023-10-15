# N = int(input())
# heights = [int(input()) for _ in range(N)]
# answer = 0
# 
# for idx, height in enumerate(heights):
#     candidates = heights[idx:]
#     admin = candidates.pop(0)
#     building = 0
#     while candidates:
#         if candidates[building] <= admin:
#             building += 1
#         else:
#             break
#     answer += building
# 
# print(answer)



N = int(input())
heights = [int(input()) for _ in range(N)]
view = []
answer = 0

for building in range(N):
    # print(view, end=" ")
    while view and view[-1] <= heights[building]:
        view.pop()
    view.append(heights[building])
    answer += len(view) - 1

print(answer)





