import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    A, B = map(str, input().split())

    cnt = A.count(B)
    cnt += len(A) - (len(B) * cnt)

    print('#{} {}'.format(t, cnt))