N= int(input())

hint = [list(map(int,input().split())) for _ in range(N)]

answer =0
for a in range(1,10):
    for b in range(1, 10):
        for c in range(1, 10):

            if(a==b or b==c or a==c):
                continue

            cnt =0
            
            for arr in hint:
                number = list(str(arr[0]))
                strike = arr[1]
                ball = arr[2]

                strike_count =0
                ball_count = 0
            
                if(a== int(number[0])):
                    strike_count+=1
                if(b== int(number[1])):
                    strike_count+=1
                if(c== int(number[2])):
                    strike_count+=1
                
                if(a== int(number[1]) or a == int(number[2])):
                    ball_count+=1
                if(b== int(number[0]) or b == int(number[2])):
                    ball_count+=1
                if(c== int(number[1]) or c == int(number[0])):
                    ball_count+=1

                if ball_count == ball and strike_count == strike:
                    cnt += 1

            if cnt == N:
                answer+=1

print(answer)