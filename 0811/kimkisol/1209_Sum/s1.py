import sys
sys.stdin = open('input.txt')
input = sys.stdin.readline

for t in range(1, 11):
    input()
    nums = []

    for _ in range(100):
        nums.append(list(map(int, input().split())))

    max_row = 0
    max_col = 0
    l_cross = 0
    r_cross = 0
    for i in range(100):
        row = 0
        col = 0
        l_cross += nums[i][i] #한 행이 넘어갈 때마다 대각선 왼쪽부터 더함
        r_cross += nums[i][99-i] #한 행이 넘어갈 때마다 대각선 오른쪽부터 더함
        for j in range(100):
            row += nums[i][j] #한 행씩 열을 돌며 더함
            col += nums[j][i] #한 열씩 행을 돌며 더함
        #max 값보다 큰 값이 나올시 교체
        if max_row < row:
            max_row = row
        if max_col < col:
            max_col = col

    #전체 행 최대값, 열 최대값, 왼쪽 대각선, 오른쪽 대각선 중 최대값 구함
    result = max(max_row, max_col, l_cross, r_cross)

    print('#{} {}'.format(t, result))