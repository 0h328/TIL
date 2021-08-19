'''
Hint 없이 혼자서 생각해서 한번에 Pass !!!
'''
import sys
sys.stdin = open('input.txt')
# from pandas import DataFrame # 진짜 편리한 도구인 것 같다

T = int(input())

for test_case in range(1, T+1):
    N = int(input()) # 행의 갯수를 정수로 받음
    A = [[0] * N for _ in range(N)] # 가로, 세로 길이가 N인 모든 요소가 0으로 초기화된 행렬 생성

    for r in range(N): # 대각선과, 첫번째 열에 있는 모든 값에 1을 넣어줌
        A[r][0] = 1
        A[r][r] = 1

    for r in range(N): # 손으로 일반항을 구해본 결과 아래처럼 구해짐, 현재 값이 0인 곳들만 아래의 일반항을 적용
        for c in range(N):
            if A[r][c] == 0:
                A[r][c] = A[r-1][c-1] + A[r-1][c]

    # print(DataFrame(A)) # 출력해보면 대각선을 기준으로 윗 부분에도 이상한(?) 값들이 생기는데 어차피 잘라서 출력할거라 걱정 No

    print('#{}'.format(test_case)) # 테스트 번호 출력
    for r in range(N): # 행을 0부터 ~ N-1 까지
        for c in range(r+1): # 열을 0부터 (0, 1), (0, 1, 2), (0, 1, 2, 3)... 와 같이
            print(A[r][c], end=' ') #해당 요소 출력, 행 기준 enter, 값 기준 띄어쓰기
        print()


