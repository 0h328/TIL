import sys
sys.stdin = open('input.txt')

T = int(input())

for case in range(T):
    A, B = input().split()
    cnt = A.count(B) + len(A) - (len(B) * A.count(B))
    print('#{} {}'.format(case + 1, cnt))
