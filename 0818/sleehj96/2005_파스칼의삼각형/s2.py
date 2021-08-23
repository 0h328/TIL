import sys


def pascal_triangle(n):
    existing_len = len(pascal_nums)

    if n == 1:
        pascal_nums.append([1, 1])
        return pascal_nums

    if n <= existing_len:
        return pascal_nums[:n]
    else:
        for k in range(existing_len, n+1):
            new_line = [1, 1]
            for idx in range(1, k):
                new_line.insert(idx, pascal_nums[k-1][idx-1] + pascal_nums[k-1][idx])
            pascal_nums.append(new_line)
        return pascal_nums


sys.stdin = open('input.txt')
T = int(input())

test_case = 1
pascal_nums = [[1]]

while test_case <= T:

    N = int(input())

    pascal_triangle(N-1)

    print('#{}'.format(test_case))
    for order in range(N):
        print(*pascal_nums[order])

    test_case += 1
