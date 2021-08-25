import sys
sys.stdin = open("input.txt")

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    value = list(map(int, input().split()))
    value.reverse()
    benefit = 0
    max_val = value[0]

    for i in range(1, N):
        if max_val < value[i]:
            max_val = value[i]

        else:
            benefit += max_val - value[i]

    print('#{} {}'.format(tc, benefit))