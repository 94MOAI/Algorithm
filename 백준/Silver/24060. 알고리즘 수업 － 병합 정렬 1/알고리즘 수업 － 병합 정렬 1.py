def mergeSort(A:list):
    global answer

    if len(A) == 1:
        return A

    mid = (len(A)+1) // 2
    left = mergeSort(A[:mid])
    right = mergeSort(A[mid:])

    i = j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            temp.append(left[i])
            i += 1
        else: # left[i] >= right[j]:
            result.append(right[j])
            temp.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        temp.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        temp.append(right[j])
        j += 1

    return result



N, K = map(int, input().split())
arr = list(map(int, input().split()))
temp = []

mergeSort(arr)

if len(temp) >= K:
    print(temp[K-1])
else:
    print(-1)