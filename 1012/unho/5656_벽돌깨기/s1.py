import sys
sys.stdin = open('input.txt')


def solution():
    pass


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())
    board = {}              # 키: 열번호 / 값: 높이별 블록값 (왼쪽 가장 위의 값, 오른쪽 가장 아래 값)

    for h in range(H):
        w = list(map(int, input().split()))
        for idx in range(len(w)):
            if w[idx]:
                board[idx] = board.get(idx, []) + [w[idx]]
    
    
    