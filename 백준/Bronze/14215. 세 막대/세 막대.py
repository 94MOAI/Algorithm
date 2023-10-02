length = list(map(int, input().split()))
length.sort()

if length[2] < length[0] + length[1]:
    print(sum(length))
else:
    length[2] = length[0] + length[1] - 1
    print(sum(length))
