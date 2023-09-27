# 이분탐색 -> 정렬되어 있어야 한다!
# N 리스트 안에 M 리스트의 요소가 있는지 확인!
def BinarySearch(A:list, target, start, end):
    while start <= end:
        mid = (start + end)//2

        if A[mid] == target:
            return print(1)
        elif A[mid] > target:
            end = mid - 1
        else: # A[mid] < target:
            start = mid + 1

    return print(0)


N = int(input())
N_lst = list(map(int, input().split()))
N_lst.sort()

M = int(input())
M_lst = list(map(int, input().split()))

for idx in range(M):
    BinarySearch(N_lst, M_lst[idx], 0, N-1)