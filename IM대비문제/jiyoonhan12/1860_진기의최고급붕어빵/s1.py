import sys
sys.stdin = open('input2.txt')

T = int(input())
for t in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive = sorted(list(map(int, input().split()))) # 도착 시간 sort
    res = 'Possible'

    if M > arrive[0]: # 첫번째 손님이 M보다 빨리 오면
        res = 'Impossible'
    else:
        i = 1
        while i <= N // K:
            customer = arrive[(i-1) * K:i * K]
            for w in range(K):
                if customer[w] < i * M:
                    res = 'Impossible'
                    break
            i += 1

    print('#{} {}'.format(t, res))