import sys
sys.stdin=open('input.txt')

N = int(input())

for tc in range(1,N+1):
    A = input()
    B = input()


    if A in B:
        ans = 1
    else:
        ans = 0

    print('#{} {}'.format(tc, ans))

        #이렇게 푸는 거 맞나,,?