import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    N, M = map(int, input().split())
    weights = list(map(int, input().split()))   # w
    loads = list(map(int, input().split()))     # t

    weights.sort(reverse=True)
    loads.sort(reverse=True)

    ans = 0
    i = j = 0
    while i < N and j < M:
        if weights[i] <= loads[j]:
            ans += weights[i]
            j += 1
        i += 1

    print('#{0} {1}'.format(tc+1, ans))
    # break
