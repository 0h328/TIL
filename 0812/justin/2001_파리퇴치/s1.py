import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    max_kill = 0
    flies = [list(map(int, input().split())) for _ in range(N)]

    """
    파리지도 - (파리채+1)
    ex. 5-2+1 = 4 -> 크기가 5짜리인 파리 지도에서 파리채의 크기가 2라면 총 4번 위아래로 이동
    """
    for r in range(N-M+1):                          # 구간합
        for c in range(N-M+1):                      # 죽인 파리수 -> 해당 변수의 위치 주의 (파리채로 다 잡고 이동한 다음 다시 잡기)
            killed_flies = 0
            for i in range(M):                      # 다시 파리채의 크기만큼 반복
                for j in range(M):
                    killed_flies += flies[r+i][c+j] # 이때 r+i & c+j를 찾는 것이 포인트
            if max_kill < killed_flies:             # 파리채로 파리를 잡고나서 최댓값 갱신 여부 결정 (조건문 위치 유의)
                max_kill = killed_flies

    print('#{} {}'.format(tc, max_kill))