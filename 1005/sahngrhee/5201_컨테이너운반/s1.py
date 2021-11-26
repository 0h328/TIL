import sys
sys.stdin = open('input.txt')

T = int(input())

for test_case in range(1, T+1):
    N, M = map(int, input().split())
    W = list(map(int, input().split()))
    T = list(map(int, input().split()))

    W = list(reversed(sorted(W)))
    T = list(reversed(sorted(T)))
    ans = 0

    for t in T:
        for w in W:
            if w <= t:
                ans += w
                W.remove(w)
                break

    print('#{} {}'.format(test_case, ans))