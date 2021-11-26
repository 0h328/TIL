import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    check = [0, 1]
    width = N // 10
    for i in range(2, width+1):                 # 마지막까지 포함되어야 하기 때문에 +1
        if i % 2:
            check.append(check[i-1]*2-1)
        else:
            check.append(check[i-1]*2+1)
    ans = check[-1]
    print('#{} {}'.format(tc, ans))