import sys
sys.stdin = open('input.txt')
import pandas
# thought process:  5분20초
# 입력값을 받아서 2차원배열 만들고,
# 맨 우측 한줄과 맨 아래 한줄을 제외하고 루프돌며,
# 확인 인덱스 기준 우측, 대각선, 아래 한칸씩 인덱스들과의 합을 구한다
# max_kills 변수에 큰 값들을 업데이트해나가고,
# 마지막에 max_val 프린트 = 정답


# 소요시간 28분 26초
for tc in range(1, int(input())+1):

    N, parichae = map(int, input().split())     # 한쪽 면의 길이와 파리채의 한쪽면 길이 입력값들
    zone = [list(map(int, input().split())) for _ in range(N)]  # 전체 2차원 배열 입력값
    max_kills = 0                               # 전체 최대 퇴치 수 초기화

    for i in range(N - parichae + 1):           # 전체 2차원 배열의 맨 우측 열과 맨 아래 행을 파리채의 길이만큼
        for j in range(N - parichae + 1):       # 제외하고 하나씩 인덱스에 접근
            kills = 0                           # 한번 내려칠때마다 퇴치 수 초기화
            for k in range(parichae):
                kills += sum(zone[i+k][j:j+parichae])   # 한번 내려 쳤을때 퇴치 수 카운트하고 퇴치 수 에 할당
            if max_kills < kills:               # 퇴치 수 가 현재 max_kills 보다 크면
                max_kills = kills               # max_kills 업데이트
    print('#{} {}'.format(tc, max_kills))       # 최종 max_kills 프린트

