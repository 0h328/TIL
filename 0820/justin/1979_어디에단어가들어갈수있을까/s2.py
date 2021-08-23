def solve():
    cnt = 0                 # 쿠션으로 인해 (1, 1)부터 인덱스 시작, 끝 인덱스는 (5, 5)
    for i in range(1, N+1): # 1부터 N까지 반복을 돌며
        x = 1
        while x <= N:             # x가 전체 단어 리스트의 크기보다 작거나 같을 때까지 반복
            if not data[i][x]:    # 가로 체크 (행우선) -> 만약 0이면
                x += 1            # 검은 영역 -> 다음을 봐야함 -> x를 증가 시키자
            else:                 # # 1이면
                blanks = 0        # 1이 몇개 연속으로 나오는지 체크하기 위한 변수
                while data[i][x]: # 해당 값이 1일 때 계속 반복
                    blanks += 1   # 채워가고
                    x += 1        # 앞으로 하나씩 이동
                if blanks == M:   # 반복 끝나고 만약 공백의 개수와 찾아야 하는 단어 개수가 같으면
                    cnt += 1      # 카운트 하나 늘리자

        y = 1                     # y 초기화 (1, 1) -> 1로 시작
        while y <= N:
            if not data[y][i]:    # 세로 체크 (열우선)
                y += 1
            else:
                blanks = 0
                while data[y][i]:
                    blanks += 1
                    y += 1
                if blanks == M:
                    cnt += 1
    return cnt

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T + 1):
    N, M = map(int, input().split())
    data = [[0] * (N + 2)]                                                    # Error Handling 을 하지 않기 위해 주변을 0으로 쿠션 만들기 -> 0으로 둘러 싸주기 위해 위쪽에 0으로
    data += [([0] + list(map(int, input().split())) + [0]) for _ in range(N)] # 입력으로 받는 값도 양 옆을 0으로
    data += [[0] * (N + 2)]                                                   # 아래쪽 0으로
    result = solve()
    print('#{} {}'.format(tc, result))