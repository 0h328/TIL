import sys
sys.stdin = open('input.txt')


def dfs(y, x, length, word):            # dfs 탐색
    if length >= 6:                     # 6번 이동했다면 종료
        word_list.add(''.join(word))
        return
    
    for k in range(4):                  # 4방향으로 탐색
        r = y + dr[k]
        c = x + dc[k]

        if 0 <= r < 4 and 0 <= c < 4:
            word.append(board[r][c])    # 현재 위치 숫자 추가
            dfs(r, c, length+1, word)   # 재귀 호출
            word.pop()                  # 현재 위치 숫자 삭제


dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

T = int(input())
answer = []

for tc in range(1, T+1):
    board = [input().split() for _ in range(4)]
    word_list = set()

    for i in range(4):                  # 시작점 순회
        for j in range(4):
            dfs(i, j, 0, [board[i][j]])
    
    answer.append('#{} {}'.format(tc, len(word_list)))

print(*answer, sep='\n')