temp = [[" "]*15 for _ in range(5)]

for i in range(5):
    example = input()

    line_len = 0
    for _ in example:
        line_len += 1

    for j in range(line_len):
        temp[i][j] = example[j]

# print(temp)
for j in range(15):
    for i in range(5):
        if temp[i][j] != " ":
            print(temp[i][j], end="")

