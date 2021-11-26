import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())                            # 배열 크기, 파리채 크기 입력
    fly = [list(map(int, input().split())) for _ in range(N)]   # 배열 입력

    max_kill = 0                                # 최대 킬수
    for i in range(N-M+1):                      # 파리채 행 기준 이동범위
        for j in range(N-M+1):                  # 파리채 열 기준 이동범위
            kill_fly = 0                        # 각 반복마다 킬수 초기화
            for r in range(i, i+M):             # 파리채 가로 길이
                for c in range(j, j+M):         # 파리채 세로 길이
                    kill_fly += fly[r][c]       # 파리채 영역 내 파리 수 합산
            if kill_fly > max_kill:             # 최댓값 구하기
                max_kill = kill_fly

    print('#{} {}'.format(tc, max_kill))