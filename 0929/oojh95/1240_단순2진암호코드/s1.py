import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]

    code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _
            in range(2)] for _ in range(2)]
    code[0][0][0][1][1][0][1] = 0
    code[0][0][1][1][0][0][1] = 1
    code[0][0][1][0][0][1][1] = 2
    code[0][1][1][1][1][0][1] = 3
    code[0][1][0][0][0][1][1] = 4
    code[0][1][1][0][0][0][1] = 5
    code[0][1][0][1][1][1][1] = 6
    code[0][1][1][1][0][1][1] = 7
    code[0][1][1][0][1][1][1] = 8
    code[0][0][0][1][0][1][1] = 9
    t = []
    ans = []
    pos = -1
    for j in range(N):
        for i in range(len(arr[j]) - 1, -1, -1):
            if arr[j][i] == 1:
                pos = i
                t = arr[j][pos-55:pos+1]
                break
        if pos > 0:
            break
    pos = len(t)-1
    while pos > 0:
        x = code[t[pos - 6]][t[pos - 5]][t[pos - 4]][t[pos - 3]][t[pos - 2]][t[pos - 1]][t[pos]]
        ans.append(x)
        pos -= 7
    if (ans[0] + (ans[1] + ans[3] + ans[5] + ans[7])*3 + ans[2] + ans[4] + ans[6]) % 10 ==0:
        print('#{} {}'.format(tc, sum(ans)))
    else:
        print('#{} {}'.format(tc, 0))


