def solve():
    for i in range(N):  # 회문은 1개 있음 -> N만큼 반복을 돌며 가로 & 세로 회문 찾기 진행
        for j in range(N - M + 1):  # 가로 검사 (N-M+1 -> 찾아야 하는 회문의 길이)
            tmp = []
            for k in range(M):  # 회문의 길이만큼 반복
                tmp.append(words[i][j + k])  # 행 고정
            if tmp == list(reversed(tmp)):  # 회문이면 반환하고 종료
                return tmp

        for j in range(N - M + 1):  # 세로 검사 (N-M+1 -> 찾아야 하는 회문의 길이)
            tmp = []
            for k in range(M):
                tmp.append(words[j + k][i])  # 열 고정
            if tmp == list(reversed(tmp)):  # 회문이면 반환하고 종료
                return tmp


import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    # N: 2차원 리스트의 크기
    # M: 찾고 싶은 회문의 길이
    N, M = map(int, input().split())
    words = [list(input()) for _ in range(N)]
    ans = ''.join(solve())
    print('#{} {}'.format(tc, ans))
