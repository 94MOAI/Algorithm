PRIME = 1234567891

def con_hash(idx, alpha):
    return (ord(alpha) - ord('a') + 1) * 31**idx % PRIME

N = int(input())
text = list(input())

answer = 0
for idx, char in enumerate(text):
    answer += con_hash(idx, char)

print(answer % PRIME)