# N X N 배열이 주어지고, M X M 파리채를 이용해 가장 많이 죽일 수 있는 파리 수를 구하는 문제
import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    area = [list(map(int, input().split())) for _ in range(N)]

    max_val = 0     # 파리 죽일 수 있는 최대값 저장할 변수
    # 가로, 세로 끝에서 M 크기만큼 떨어져 있어야 파리채로 잡을 수 있으므로 N-M+1로 반복 범위 설정
    for k in range(N - M + 1):
        for l in range(N - M + 1):
            total = 0   # 현재 파리채로 잡을 수 있는 마리수 저장할 임시 변수
            for m in range(M):  # 한 행씩 내려가면서 파리 잡은 수 더해줌
                total += sum(area[k+m][l:l+M])
            if max_val < total:
                max_val = total

    print('#{} {}'.format(tc, max_val))