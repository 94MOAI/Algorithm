A = [int(input()) for _ in range(9)]

mx_idx = 0
mx = 0
for idx, number in enumerate(A):
    if mx < number:
        mx = number
        mx_idx = idx+1

print(mx, mx_idx)