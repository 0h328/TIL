import sys
sys.stdin = open('input.txt')


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    schedule = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: (x[1], x[0]))     # 끝나는 시간을 기준으로 오름차순
    end_time = 0
    answer = 0

    for e in schedule:              # 스케줄 모두 순회
        if end_time <= e[0]:        # 마지막으로 끝난 시간이 시작시간보다 작거나 같으면
            answer += 1
            end_time = e[1]

    print('#{} {}'.format(tc, answer))