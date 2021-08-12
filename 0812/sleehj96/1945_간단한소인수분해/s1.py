import sys

sys.stdin = open('input.txt')

T = int(input())

i = 1
while i <= T:

    N = int(input())
    prime_list = [2, 3, 5, 7, 11]

    e_list = [0, 0, 0, 0, 0]

    # print('1111111111')
    n = 0

    while n < len(e_list):
        if not (N % prime_list[n]):
            # print('1111')
            N //= prime_list[n]
            e_list[n] += 1
            continue
        n += 1

    # print(e_list)

    ans_str = ' '.join(map(str, e_list))
    print(f'#{i} {ans_str}')

    # print(main_array)

    i += 1