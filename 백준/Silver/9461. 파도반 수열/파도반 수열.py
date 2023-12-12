P = [0 for i in range(101)]
P[1] = P[2] = P[3] = 1

for i in range(4, 100+1):
    P[i] = P[i-3] + P[i-2] 

for _ in range(int(input())):
    print(P[int(input())])