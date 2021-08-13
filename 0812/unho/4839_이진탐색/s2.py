import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    P, A, B = map(int, input().split())
    answer = '0'

    search_a = P
    search_b = P

    P //= 2

    while P >= 0:
        if search_a == A and search_b == B:
            answer = '0'
            break
        elif search_a == A:
            answer = 'A'
            break
        elif search_b == B:
            answer = 'B'
            break

        if search_a > A:
            search_a -= P
        elif search_a < A:
            search_a += P

        if search_b > B:
            search_b -= P
        elif search_b < B:
            search_b += P


    print('#{} {}'.format(tc, answer))