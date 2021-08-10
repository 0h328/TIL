import sys
sys.stdin = open('input.txt')

T = int(input())
for test_case in range(1, T+1):
    N = int(input())
    height = list(map(int,input().split()))

    result = 0

    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if height[i] > height[j]:
                cnt += 1

            if cnt > result:
                result = cnt

    print('#{} {}'.format(test_case, result))





