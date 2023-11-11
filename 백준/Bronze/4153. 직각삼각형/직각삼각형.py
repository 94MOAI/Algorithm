while True:
    arr = list(map(int, input().split()))
    if not sum(arr):
        quit()
    arr.sort()
    if arr[0]**2 + arr[1]**2 == arr[2]**2:
        print('right')
    else:
        print('wrong')
    