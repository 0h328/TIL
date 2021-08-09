import sys
sys.stdin = open('input.txt')

T = int(input())

for test in range(T):
    N = int(input())
    result = [0]*12
    cnt = 0
    while N > 0:
        result[N%10] += 1
        N //= 10

    for i in range(2,len(result)):
        if result[i] == 3 or result[i-1] == 3 or result[i-2] == 3:
            cnt += 1
        if result[i] == 1 and result[i-1] == 1 and result[i-2] == 1:
            cnt += 1

    if cnt>=2:
        print(True)
    else:
        print(False)