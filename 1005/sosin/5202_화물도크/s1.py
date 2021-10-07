import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    result = 0
    N = int(input())
    schedules = [list(map(int, input().split()))+[1] for _ in range(N)]
    schedules = sorted(schedules, key=lambda i : i[1])
    i = 0
    while i < N-1:
        next_i = N
        temp = 24
        for j in range(i+1, N):
            if schedules[i][1] <= schedules[j][0] and temp > schedules[j][1]:
                temp = schedules[j][1]
                schedules[j][2] += schedules[i][2]
                next_i = j
        i = next_i
    result = max(d for s, e, d in schedules)
    print('#{} {}'.format((T+1), result))

#1 4
#2 4
#3 5