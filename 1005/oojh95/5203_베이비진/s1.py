import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    arr = list(map(int, input().split()))
    a_arr = [0] * 10
    b_arr = [0] * 10
    result = 0
    for i in range(0, 12, 2):
        a_arr[arr[i]] += 1
        b_arr[arr[i+1]] += 1

        if i >= 4:
            for j in range(10):
                if a_arr[j] >= 3:
                    result = 1
                if j <= 7 and a_arr[j] and a_arr[j+1] and a_arr[j+2]:
                    result = 1
                if b_arr[j] >= 3:
                    result += 2
                if j <= 7 and b_arr[j] and b_arr[j+1] and b_arr[j+2]:
                    result += 2
                if result != 0:
                    break
        if result != 0:
            break
    if result > 2:
        result = 0
    print('#{} {}'.format(tc, result))