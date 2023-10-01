import sys
input = sys.stdin.readline

# def quick_sort(A, start, end):
#     '''
#     :param A: 정렬을 진행할 배열
#     :param start: 정렬을 시작할 인덱스
#     :param end: 정렬을 끝낼 인덱스
#     :return: 원소가 1개만 존재할 경우 그대로 종료
#     '''
# 
#     if start >= end:
#         return
# 
#     pivot = start # pivot은 정렬을 위한 기준 인덱스
#     left, right = start + 1, end
# 
#     while left <= right:
#         # 피벗보다 작은 데이터를 찾을 때까지 반복
#         while left <= end and A[left] <= A[pivot]:
#             left += 1
#         # 피벗보다 큰 데이터를 찾을 때까지 반복
#         while right > start and A[right] >= A[pivot]:
#             right -= 1
#         if left > right:
#             A[right], A[pivot] = A[pivot], A[right]
#         else:
#             A[right], A[left] = A[left], A[right]
# 
#     quick_sort(A, start, right-1)
#     quick_sort(A, right+1, end)


N = int(input())
number = [0]*N

for idx in range(N):
    number[idx] = int(input())

# quick_sort(number, 0, N-1)
number.sort()

for idx in range(N):
    print(number[idx])