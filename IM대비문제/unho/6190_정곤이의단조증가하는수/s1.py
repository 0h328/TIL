import sys
sys.stdin = open('input.txt')

test_case = int(input())

for tc in range(1, test_case+1):
    N = int(input())
    in_list = list(map(int, input().split()))

    num_list = []
    for i in range(N-1):
        for j in range(i+1, N):
            mul_num = mul_answer = in_list[i] * in_list[j]

            tmp = 10
            while mul_num > 0:
                if tmp < mul_num%10:
                    break
                tmp = mul_num%10
                mul_num //= 10
            else:
                num_list.append(mul_answer)

    if not num_list:
        answer = -1
    else:
        answer = max(num_list)

    print('#{} {}'.format(tc, max(num_list)))