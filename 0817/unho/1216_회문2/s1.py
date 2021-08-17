'''
1. 4중 for??? - 시간이 너무 오래걸림
2.
'''

import sys
sys.stdin = open('input.txt')




for _ in range(1):
    tc = int(input())
    board = [input().strip() for _ in range(100)]
    board.extend(map(lambda x: ''.join(x), zip(*board)))        # 배열의 세로 부분 추가
    answer = 0

    for e in board:                                             # 가로 / 세로 한줄의 문자열
        for i in range(100):                                    # 한 문자열의 길이 100 / 문자열 시작 인덱스
            for j in range(100, i, -1):                         # 가장 긴걸 찾아야 하므로 길이 긴거부터 검색 / 문자열 끝 인덱스
                tmp = e[i:j]                                    # 문자열 슬라이싱
                if tmp == tmp[::-1] and answer < len(tmp):      # 해당 시작점의 문자열이 해당 길이가 회문이고, 정답의 길이보다 길면
                    answer = len(tmp)                           # 새로운 정답, 현재 시작 인덱스에서 가장 긴 문자열이므로 break
                    break
                elif len(tmp) <= answer:                        # 문자열의 길이가 정답보다 짧아지면 break
                    break

    print('#{} {}'.format(tc, answer))