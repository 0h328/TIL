'''
백트래킹 활용하여 연산 줄임
'''

import sys
sys.stdin = open('input.txt')



def solution(i, tmp_sum):                                       # 행 인덱스 / 사용한 열 인덱스 번호 / 현재 단계까지의 합
    global answer

    #Base Case
    if tmp_sum > answer:                                        # 현재 단계까지의 합이 정답보다 큰 경우 재귀 종료
        return
    elif i == N:                                                # 행 인덱스가 N일때 정답에 현재까지 합 대입
        answer = tmp_sum
        return

    for c in range(N):                                          # 열 인덱스 반복
        if not use_column[c]:                                   # 현재 열이 사용된 열이 아니면
            use_column[c] = 1                                   # 사용열 리스트에 추가
            solution(i+1, tmp_sum + board[i][c])                # 재귀함수 (행 인덱스 / 사용한 열 인덱스 리스트 / 현재 단계까지 합)
            use_column[c] = 0                                   # 사용한 열 인덱스에서 마지막 열 삭제



test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    board = [list(map(int, input().split())) for _ in range(N)]
    answer = 9 * N                                              # 현재 최소합 (현재 보드에서 구할수있는 최고합)
    use_column = [0] * N

    solution(0, 0)                                              # 백트래킹 활용 재귀함수 호출

    print('#{} {}'.format(tc, answer))