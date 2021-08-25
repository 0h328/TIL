def solve(left, right):
    # 가위: 1, 바위: 2, 보: 3
    if left == right:         # 분할하다가 같아진 경우 
        return right          # left or right 어느 쪽을 반환해도 상관없음
    # 플레이어 선정 작업 진행
    """
    문제에 제시된 조건 그대로 표현
    win1: i ~ (i+j) // 2
    win2: (i+j) // 2 + 1 ~ j 
    """
    player1 = solve(left, (left+right)//2)
    player2 = solve((left+right)//2+1, right)

    # 위에서 대결을 붙는 사람을 선정했으면(분할) 대결 시작
    if cards[player1] == cards[player2]:    # 만약 win1과 win2의 카드가 같다면
        return player1                      # (문제에 제시된 조건) 번호가 작은 쪽을 선택
    else:                                   # 카드가 다르다면
        # 가위 vs 바위 -> 바위
        if cards[player1] == 1 and cards[player2] == 2:
            return player2
        # 가위 vs 보 -> 가위
        elif cards[player1] == 1 and cards[player2] == 3:
            return player1
        # 바위 vs 가위 -> 바위
        elif cards[player1] == 2 and cards[player2] == 1:
            return player1
        # 바위 vs 보 -> 보
        elif cards[player1] == 2 and cards[player2] == 3:
            return player2
        # 보 vs 가위 -> 가위
        elif cards[player1] == 3 and cards[player2] == 1:
            return player2
        # 보 vs 바위 -> 보
        elif cards[player1] == 3 and cards[player2] == 2:
            return player1

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())                                # 인원수
    cards = [0] + list(map(int, input().split()))   # N명이 고른 카드가 번호순으로 주어지기 때문에 인덱스 관리 편의를 위해 0 추가
    ans = solve(1, N)                               # 1부터 N까지의 사람들이 게임을 진행
    print('#{} {}'.format(tc, ans))

"""
포인트
1) 분할 정복 
- 나눌 수 없는 최대로 작은 부분까지 분할(left == right)하여 승자를 결정하고 
- 해당 승자를 위로 올려 다시 대결 후 승자를 결정

2) 재귀 호출
재귀 호출로 인해 호출 stack에 쌓여있는 함수가 종료될 경우 나를 마지막으로 호출했던 곳으로 돌아감
"""