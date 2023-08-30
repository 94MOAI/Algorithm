def reverse_number(argm):
    
    result = 0
    while argm % 10:
        result *= 10
        result += argm%10
        argm //= 10

    return result


A, B = map(int, input().split())

print(max(reverse_number(A), reverse_number(B)))