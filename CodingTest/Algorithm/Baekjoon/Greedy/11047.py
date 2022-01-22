import sys
sys.stdin = open('input.txt')

N, K = map(int, input().split())
coins = [int(input()) for _ in range(N)]
coins.sort(reverse=True)    # 최솟값을 구해야하므로 큰 동전 단위부터 정렬

cnt = 0
for coin in coins:
    if coin <= K:           # 주어진 합보다 작은 경우에만 가능
        cnt += K // coin    # 해당 동전으로 만들 수 있는 개수 더하기
        K %= coin           # 해당 동전 전부 사용 후, 그 다음 동전 사용 여부 판정 위해 나누기

print(cnt)