for _ in range(int(input())):
    quiz = input()

    score = 0
    bonus = 1
    for el in quiz:
        if el == 'O':
            score += bonus
            bonus += 1
        else:
            bonus = 1

    print(score)