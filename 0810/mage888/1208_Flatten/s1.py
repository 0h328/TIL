import sys
sys.stdin = open('input.txt')

T = 10

for test_case in range(1, T+1):
    N = int(input())
    boxs = list(map(int, input().split()))

    result = 0

    for k in range(N):
        boxs[boxs.index(max(boxs))] -= 1
        boxs[boxs.index(min(boxs))] += 1
        result = max(boxs)-min(boxs)

    print('#{} {}'.format(test_case, result))
