import sys

sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T + 1):
    N, M = map(int, input().split())
    ans = '0'
    temp_ans = ''
    if M == 0:
        pass
    else:
        while M != 1:
            temp_ans += str(M % 2)
            M = M // 2
        temp_ans += str(M)
    if len(temp_ans) >= 1:
        ans = temp_ans[::-1]
    check = 0
    for k in range(N):
        if ans[len(ans)-k-1] == '1':
            check = 1
        else:
            check = 0
            break
    print(ans)
    if check == 1:
        print('#{} {}'.format(tc, 'ON'))
    else:
        print('#{} {}'.format(tc, 'OFF'))
