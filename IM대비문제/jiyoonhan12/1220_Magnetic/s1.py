import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    L = int(input()) # 한 변의 길이
    arr = [list(map(int, input().split())) for _ in range(L)]
    ans = 0

    for j in range(100): # 열 순회
        col = ''
        for i in range(100):
            if arr[i][j] != 0: # 1이거나 2일 때만 col에 추가
                col += str(arr[i][j])
        temp = col.count('12') # '12'가 연달아 붙어있을 때만 count
        ans += temp

    print('#{} {}'.format(t, ans))

    # 열에 1개만 있을 경우 교착 상태 x
    # else
    # 열에 n개가 있는데 그 n개가 다 같을 경우도 pass
    # 열에 2개 이상 있는데 AB가 연달아 나오는 경우만 count