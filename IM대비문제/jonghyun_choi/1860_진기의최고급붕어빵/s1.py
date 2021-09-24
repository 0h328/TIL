import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    N, M, K = map(int, input().split())
    data = list(map(int, input().split()))
    time = [0] * (max(data) + 1)
    for i in range(1, len(time)):
        if i % M == 0:
            time[i] = time[i - 1] + K
        else:
            time[i] = time[i - 1]
    res = 'Possible'
    for i in data:
        if time[i] <= 0:
            res = 'Impossible'
        else:
            for j in range(i - (i%M), len(time)):
                time[j] -= 1
    print('#{} {}'.format(case + 1, res))

