import sys
sys.stdin = open('input.txt', 'r')

T = int(input())

for tc in range(1, T + 1):
    N, B = map(int, input().split())
    heights = list(map(int, input().split()))
    possible = [0]
    answer = 200001
    # DP
    for height in heights:
        p = len(possible)
        for i in range(p):
            tmp = possible[i] + height
            if B <= tmp and answer > tmp - B:
                answer = tmp - B
            possible.append(tmp)

    print('#{} {}'.format(tc, answer))
