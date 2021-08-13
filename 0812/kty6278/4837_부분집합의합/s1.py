import sys
sys.stdin = open('input.txt')

testcase = int(input())
arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
num = len(arr)

for test in range(testcase):
    n, k = list(map(int, input().split()))

    result = 0
    for i in range(1 << num):
        num_arr = []
        for j in range(num):
            if i & (1 << j):
                num_arr.append(arr[j])
        if len(num_arr) == n and sum(num_arr) == k:
            result += 1

    print('#{} {}'.format(test + 1, result))