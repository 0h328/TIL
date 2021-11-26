import sys


def pascal_triangle(n):
    if n == 1:
        return [1]
    else:
        if n == 2:
            return [1, 1]
        else:
            ans_list = pascal_triangle(2)
            for idx in range(1, n-1):
                ans_list.insert(idx, pascal_triangle(n-1)[idx-1] + pascal_triangle(n-1)[idx])
            return ans_list


sys.stdin = open('input.txt')
T = int(input())

test_case = 1

while test_case <= T:

    N = int(input())

    print('#{}'.format(test_case))
    for k in range(N):
        print(*pascal_triangle(k+1))

    test_case += 1
