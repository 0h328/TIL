import sys
sys.stdin = open('input.txt')


def check_b(arr):
    result = []
    for i in range(len(arr)):
        arr[i] = (arr[i] + 1) % 2
        val = 0
        for j in range(len(arr)):
            val += 2**(len(arr)-1-j)*arr[j]
        result.append(val)
        arr[i] = (arr[i] + 1) % 2
    return result


def check_t(arr):
    result = []
    for i in range(len(arr)):
        arr[i] = (arr[i] + 1) % 3
        val = 0
        for j in range(len(arr)):
            val += 3**(len(arr)-1-j)*arr[j]
        result.append(val)
        arr[i] = (arr[i] + 1) % 3
        val = 0
        for j in range(len(arr)):
            val += 3 ** (len(arr) - 1 - j) * arr[j]
        result.append(val)
        arr[i] = (arr[i] + 1) % 3

    return result

T = int(input())
for tc in range(1, T+1):
    num_b = list(map(int, input()))
    num_t = list(map(int, input()))
    result_b = check_b(num_b)
    result_t = check_t(num_t)
    result = 0
    for i in range(len(result_b)):
        for j in range(len(result_t)):
            if result_b[i] == result_t[j]:
                result = result_b[i]
                break
        if result > 0:
            break
    print('#{} {}'.format(tc, result))
