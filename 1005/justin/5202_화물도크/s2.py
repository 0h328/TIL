import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    schedule = [list(map(int, input().split())) for i in range(N)]
    schedule.sort(key=lambda x: x[1])                               # 종료 시간 순으로 정렬
    ans = 0                                                         # 작업수
    end = 0                                                         # 앞 작업의 종료 시간
    for i in range(N):                                              # 모든 작업에 대해
        if end <= schedule[i][0]:                                   # 앞 작업 이후에 시작하면
            ans += 1                                                # 작업을 추가하고
            end = schedule[i][1]                                    # 종료시간을 새 작업으로 수정
    print('#{} {}'.format(tc, ans))
