import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(T):
    K, N, M = map(int, input().split())
    m = list(map(int, input().split()))

# m을 담아주면 되지 M에
# 거리에 닿으면(안쪽이면) -1씩해서 찾고, 안 닿으면 0


    print('#{} {}'.format(tc+1, ))
