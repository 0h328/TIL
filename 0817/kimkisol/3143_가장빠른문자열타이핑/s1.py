import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    A, B = input().split()

    cnt_B = A.count(B)
    result = len(A) - (len(B) - 1) * cnt_B

    print('#{} {}'.format(t, result))