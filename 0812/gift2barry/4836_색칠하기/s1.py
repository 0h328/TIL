import sys
sys.stdin = open('input.txt')


# 소요시간 1시간 20분
for tc in range(1, int(input())+1):

    num = int(input())           # 생상 힙히는 횟수 인풋값
    arr = [[0]*10 for _ in range(10)]   # 숫자 0 으로 채워진 고정값 크기의 2차원 배열 생성
    cnt = 0                      # 보라색 개수 카운터 초기화

    for idx in range(num):       # 페인트 횟수 만큼 반복
        c = list(map(int, input().split()))     # 페인트 범위 인풋값 (1번씩)
        if c[-1] == 1:          # 빨간색이면
            r = c[0:4]          # 빨간색 리스트에 할당
            for i in range(r[2]-r[0]+1):        # 빨간색 색칠 작업
                for j in range(r[3]-r[1]+1):
                    if arr[r[0]+i][r[1]+j] == 0:    # 페인트질 안했으면
                        arr[r[0]+i][r[1]+j] = 1     # 빨간색 페인트
                    elif arr[r[0]+i][r[1]+j] == 2:  # 이미 파란색이 있으면
                        arr[r[0] + i][r[1] + j] = 3 # 보라색으로 페인트
                        cnt += 1                    # 보라색 카운터 +1

        else:                   # 아니면
            b = c[0:4]          # 파란색 할당
            for i in range(b[2]-b[0]+1):        # 파란색 색칠 작업
                for j in range(b[3] - b[1] + 1):
                    if arr[b[0] + i][b[1] + j] == 1:    # 이미 빨간색이면
                        arr[b[0] + i][b[1] + j] = 3     # 보라색으로 색칠
                        cnt += 1
                    else:                               # 아니면
                        arr[b[0] + i][b[1] + j] = 2    # 파란색으로 색칠

    print('#{} {}'.format(tc, cnt))