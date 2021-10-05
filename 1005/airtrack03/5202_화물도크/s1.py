import sys
sys.stdin = open('input.txt')

T = int(input())

def dock(data):
    cnt = 0
    end_time = 0
    for car in data:
        if car[0] >= end_time:
            cnt += 1
            end_time = car[1]

    return cnt

for tc in range(1, T+1):
    N = int(input())
    data = [list(map(int, input().split())) for _ in range(N)]

    data.sort(key=lambda x:(x[1], x[0]))

    ans = dock(data)

    print('#{} {}'.format(tc, ans))

