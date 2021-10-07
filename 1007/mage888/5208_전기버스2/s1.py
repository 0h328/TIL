import sys
sys.stdin = open('input.txt')

def dfs(start):
    global cnt, tmp

    if tmp < cnt:     # 충전횟수가 정류장 수보다 많은 경우는 말이 안됨
        return

    for i in range(start + b[start], start, -1):
        cnt += 1
        dfs(i)
        cnt -= 1

    if start == tmp:  # 충전횟수랑 정류장 수랑 같은 경우
        if cnt < tmp:
            tmp = cnt

T = int(input())
for tc in range(1, T+1):
    data = list(map(int, input().split()))
    s = data[0]     # s = station
    b = data[1:]    # b = battery
    tmp = s
    cnt = 0         # 충전횟수

    dfs(1)

    print('#{} {}'.format(tc, tmp-1))