import sys
sys.stdin = open('input.txt')

for _ in range(10):
    N = int(input())
    arr = [[] for _ in range(100)]
    result = 0 # 결과 저장

    for i in range(100): # 리스트 입력 받기
        arr[i] = list(map(int, input().split()))

    for i in arr: # 행 합 비교
        result = max(result, sum(i))

    for i in zip(*arr): # 열 합 비교
        result = max(result, sum(i))

    # left_down = 0 # 문제 이상으로 주석 처리(설명상에는 필요하나, 답에는 필요 없음)
    # right_down = 0
    # for i in range(100): # 좌하향, 우하향 대각선 합계 구하기
    #     left_down += arr[100-i][i]
    #     right_down += arr[i][100-i]
    # result = max(left_down, right_down, result) # 최대값 뽑기

    print('#{} {}'.format(N, result))