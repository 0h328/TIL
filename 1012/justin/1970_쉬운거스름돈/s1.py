import sys
sys.stdin = open('input.txt')
T = int(input())
coins = [50000, 10000, 5000, 1000, 500, 100, 50, 10]   # 큰 단위부터 배치
for tc in range(1, T+1):
    changes = int(input())                             # 잔돈
    ans = [0] * len(coins)                             # 돈의 단위 체크

    for i in range(len(coins)):
        if coins[i] > changes:                         # 쓰려는 돈이 잔돈보다 크면 넘어가고
            continue
        ans[i] = changes // coins[i]                   # 쓸 수 있는 최대 개수 체크
        changes %= coins[i]                            # 나머지 잔돈 갱신
        if not changes:                                # 더 이상 거슬러 줘야 하는 잔돈이 없다면 종료
            break

    print('#{}'.format(tc))
    print(*ans)