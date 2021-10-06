import sys
sys.stdin = open('input.txt')

T = int(input())

def find_max(cnt, start):   # 바꾼 횟수와, 바꿀 위치를 인자로 받음
    global ans
    if cnt == change or start == N-1:   # 바꿀 횟수를 모두 썼거나 바꿀 위치가 마지막 인덱스인 경우
        og = (data[-2], data[-1])
        if cnt < change:    # 바꿀 횟수가 남아있는 경우
            if (change - cnt) & 1:
                data[-1], data[-2] = data[-2], data[-1]
        result = ''.join(data)
        data[-2], data[-1] = og     # 데이터 초기화
        if int(ans) < int(result):
            ans = result
        return
    else:
        for i in range(start+1, N):
            data[start], data[i] = data[i], data[start] # 바꿀 위치 start의 다음 인덱스부터 차례로 변경
            find_max(cnt+1, start+1)    # 해당 위치 바꾸고 진행
            data[start], data[i] = data[i], data[start] # 바꾸기 전으로 초기화
            find_max(cnt, start+1)  # 해당 위치는 바꾸지 않은 상태로 진행


for tc in range(1, T+1):
    data, change = input().split()
    data = list(data)   # 초기 리스트
    N = len(data)   # 리스트의 길이
    change = int(change)    # 바꿔야할 횟수

    ans = '0'

    find_max(0, 0)

    print('#{} {}'.format(tc, ans))



