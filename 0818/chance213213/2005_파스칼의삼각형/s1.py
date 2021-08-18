import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    org_list = [0, 1, 0]
    ans = [[0, 1, 0]]


    for i in range(N-1):
        new_list = [0]
        for j in range(len(ans[i])-1):
            new_val = ans[i][j] + ans[i][j+1]
            new_list.append(new_val)

        new_list.append(0)
        ans.append(list(new_list))

    print('#{}'.format(tc))
    for i in range(N):
        print(*ans[i][1:-1])