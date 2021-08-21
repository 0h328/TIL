def solve(data):
    for i in range(9):             # 반복을 돌며
        if len(set(data[i])) != 9: # row 확인 -> 중복 제거했을 때 길이가 9가 아니면 중복된 요소 존재
            return 0
        col = set()
        small = set()
        for j in range(9):                # 다시 반복을 돌리며
            col.add(data[j][i])
            if i % 3 == 0 and j % 3 == 0: # 3 * 3 박스 확인 -> i와 j가 0, 3, 6 인곳을 찾아
                for k in range(3):
                    for z in range(3):
                        small.add(data[i+k][j+z])
                if len(small) != 9:       # small에 중복이 있는 경우 종료
                    return 0
        if len(col) != 9:                 # col에 중복이 있는 경우 종료
            return 0
    return 1                              # 위의 모든 로직을 다 통과하면 제대로 생성된 스도쿠 판

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    data = [list(map(int, input().split())) for _ in range(9)]
    ans = solve(data)
    print('#{} {}'.format(tc, ans))