import sys
sys.stdin = open('input.txt')

T = int(input())

case_num = 1
while case_num <= T:
    A, B = input().split()

    cnt = A.count(B)

    print('#{0} {1}'.format(case_num, len(A) - cnt * (len(B) - 1)))
    case_num += 1
