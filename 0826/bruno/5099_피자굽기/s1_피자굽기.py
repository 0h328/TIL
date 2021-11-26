import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())    # 화덕 크기, 피자 갯수
    C = list(enumerate(map(int, input().split()), start=1))     # 피자번호와 치즈양 동시저장
    Q = [[idx, cheese] for idx, cheese in C]    # 튜플을 리스트로 바꾸어 저장
    in_oven = Q[:N]     # 화덕 안의 피자
    ready = Q[N:]       # 밖에서 대기중인 피자

    while len(in_oven) > 1:     # 화덕 안에 피자가 1개 남을 때까지 반복
        in_oven[0][1] //= 2     # 맨 앞(화덕입구) 피자의 치즈 녹이기
        if in_oven[0][1] != 0:  # 다 녹은게 아니라면
            in_oven.append(in_oven[0])  # 맨 뒤로 이동
            in_oven.pop(0)              # 맨 앞에서 제거
        else:               # 다 녹았다면
            in_oven.pop(0)  # 맨 앞에서 제거
            if len(ready):  # 대기중인 피자가 있다면
                in_oven.append(ready.pop(0))    # 대기 리스트에서 제거하고 화덕 안에 추가
        if len(in_oven) == 1:   # 화덕 안에 피자가 한 개 남았다면
            print('#{} {}'.format(tc, in_oven[0][0]))   # 그 피자의 번호 출력
