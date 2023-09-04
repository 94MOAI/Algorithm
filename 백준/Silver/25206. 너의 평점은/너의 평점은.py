score = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0.0]
grade = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']

info = [list(input().split()) for _ in range(20)]

total_grade = total_score = 0
for idx in range(20):
    if info[idx][2] == 'P':
        continue
    total_grade += float(info[idx][1])
    total_score += float(info[idx][1]) * score[grade.index(info[idx][2])]

result = total_score/total_grade
print(result)