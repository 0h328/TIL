import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    ans = 1
    data = [list(map(int, input().split())) for _ in range(9)]
    for i in range(9):                    # row 검사
        visited = [0] * 10                # 숫자와 인덱스를 맞춰주기 위해 10칸 생성
        for j in range(9):
            visited[data[i][j]] += 1    
            if visited[data[i][j]] > 1:   # 1보다 크면 중복된 숫자가 있다는 의미 -> 실패
                ans = 0
                break
        if ans == 0:
            break

    for i in range(9):                    # col 검사
        visit = [0] * 10
        for j in range(9):
            visit[data[j][i]] += 1
            if visit[data[j][i]] > 1:
                ans = 0
                break
        if ans == 0:
            break

    for i in range(0, 9, 3):              # 작은 회문판 검사
        for j in range(0, 9, 3):
            visited = [0] * 10
            for k in range(3):            # 파리잡기처럼 큰 박스안에 작은 박스가 있는 구조
                for z in range(3):
                    visited[data[i+k][j+z]] += 1
                    if visited[data[j][i]] > 1:
                        ans = 0
                        break
                if ans == 0:
                    break
            if ans == 0:
                break
        if ans == 0:
            break
    print('#{} {}'.format(tc, ans))