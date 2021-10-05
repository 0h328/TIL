import sys
sys.stdin = open('input.txt')

# 8개만 맞는 코드... 반례를 생각하지 못하겠다....ㅠㅠㅠㅠㅠㅠㅠㅠㅠ
# 대각선 처리해주고
# 1에서 시작하는거 처리해주고
# 1에서 끝나는거 해줘야하는건가.. 이걸 절대 내코드에서 구현을 할 방법이 없넹..


def solve(row):
    global result, cnt, min_value
    if cnt == n:  # 더해야하는 값의 수가 n이랑 같아지는 경우
        if result < min_value: # 결과값이랑 계속 비교하면서 갱신해주기
            min_value = result
            return

    for j in range(n):  # 행을 지켜볼 예정
        if row != j and not visited_col[j]: # 행과 열이 같지 않은 경우와//행이 방문하지 않은 경우
            if not visited[j][row]:         # 반대로 접었을때 대각선 방향에 존재하는 것이 방문하지 않은 경우 전체 방문 여부
                visited[row][j] = 1         # 전체 방문 처리
                visited_col[j] = 1          # 헹 방문 처리
                cnt += 1                    # 더해줄 값 += 1
                result += num[row][j]       # 결과에다가 지니고 있는 값 더하기

                solve(row+1)

                result -= num[row][j]      # 값 복귀시키기
                visited_col[j] = 0
                visited[row][j] = 0
                cnt -= 1


for tc in range(int(input())):
    n = int(input())
    num = [list(map(int, input().split())) for _ in range(n)]
    visited_col = [0 for _ in range(n)]
    visited = [[0]*n for _ in range(n)]
    result = 0
    cnt = 0
    min_value = 999999999

    visited_list = []
    solve(0)
    print('#{} {}'.format(tc+1, min_value))