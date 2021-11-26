"""
핵심 컨셉
- 지나온 길을 다시 돌아오는 일이 없도록 1을 0으로 바꾸자
- 가장 직관적인 방식
"""
import sys
sys.stdin = open('input.txt')
for tc in range(1, 11):
    T = int(input())
    ladder = [list(map(int, input().split())) for _ in range(100)]
    i = len(ladder) - 1 # 세로 이동 index -> 가장 아래부터 시작
    j = 0               # 가로 이동 index
    for x in range(len(ladder)):
        if ladder[i][x] == 2:   # 가장 바닥에서 2를 만나면
            i -= 1              # 위로 올라감
            j = x               # 그리고 그때의 인덱스 기억하고 시작
    while i != 0:               # 사다리 최상단에 도착하기 전까지 반복
        if j == 0:              # 1-1. 왼쪽 벽일 때
            if ladder[i][j + 1] == 1:   # 오른쪽에 1이 있는지 확인해서 있으면
                ladder[i][j] = 0        # 오른쪽으로 이동하기 전에 떠나기전 자신의 자리를 0으로 만들어주고
                j += 1                  # 오른쪽으로 이동하고
            else:                       # 없으면
                i -= 1                  # 위로 이동
        elif j == len(ladder) - 1:      # 1-2. 오른쪽 벽이면
            if ladder[i][j - 1] == 1:   # 왼쪽에 1이 있는지 확인해서 있으면
                ladder[i][j] = 0        # 왼쪽 이동하기 전에 떠나기전 자신의 자리를 0으로 만들어주고
                j -= 1                  # 왼쪽으로 이동하고
            else:                       # 없으면
                i -= 1                  # 위로 이동
        else:                           # 2 벽을 만나지 않았다면

            if ladder[i][j-1] == 1:     # 만약 왼쪽에 1이 있으면 왼쪽으로 1 이동 (벽이 아니기 때문에 index 에러x)
                ladder[i][j] = 0        # 지나왔던 자리는 0으로 변경 -> 그래야 다시 가지 않음
                j -= 1
            elif ladder[i][j+1] == 1:   # 만약 오른쪽에 1이 있으면 오른쪽으로 1 이동
                ladder[i][j] = 0        # 지나왔던 자리는 0으로 변경 -> 그래야 다시 가지 않음
                j += 1
            else:                       # 없다면 위로 올라감
                i -= 1
    print('#{} {}'.format(tc, j))