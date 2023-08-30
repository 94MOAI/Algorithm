ONE_DAY = 24*60

H, M = map(int, input().split())

TIME = H*60+M-45

if TIME <= 0:
    TIME += ONE_DAY

HOUR = TIME//60
if HOUR == 24:
    HOUR = 0
MINUTE = TIME%60

print(HOUR, MINUTE)
