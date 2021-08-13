import sys
sys.stdin = open('input.txt')

T = int(input())

for i in range(T):
    list1 = [[0] * 10 for _ in range(10)]
    N = int(input())
    cnt = 0
    for k in range(N):
        a, b, c, d, e = map(int, input().split())
        for t in range(a, c + 1):
            for j in range(b, d + 1):
                if list1[t][j] == 0:
                    list1[t][j] = 1
                else:
                    cnt += 1
    print('#{} {}'.format(i + 1, cnt))
