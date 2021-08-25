'''
다시 풀어보기
'''

import sys
sys.stdin = open('input.txt')


def solution(board, m):
    for e in board:                         # 문자열 한줄
        for i in range(100-m+1):            # 문자열에서 0번 인덱스부터 시작
            for j in range(m//2):           # 길이의 반만큼
                if e[i+j] != e[i+m-1-j]:    # 맨 앞과 맨뒤를 확인, 점점 안쪽으로 들어오며 확인
                    break                   # 회문이 안되면 다음 반복
            else:                           # 회문이 있으면 문자열 길이 반환
                return m
    return -1                               # 회문이 하나도 없다면 -1 반환


for _ in range(1, 11):
    tc = int(input())
    board1 = [input() for _ in range(100)]          # 가로
    board2 = [''.join(e) for e in zip(*board1)]     # 세로
    board = board1 + board2
    answer = 1

    for i in range(2, 101):
        if i > answer + 2:                  # 값이 2개가 늘어났을때까지 회문 판단을 했는데, 둘다 회문이 아니였으면 양 옆에 아무리 늘어나도 회문이 아님
            break                           # 시간 단축을 위해 종료
        if answer < solution(board, i):     # 다음 글자를 늘려서 회문 판단을 했는데, 회문이면 새로운 정답으로 저장
            answer = i

    print('#{} {}'.format(tc, answer))