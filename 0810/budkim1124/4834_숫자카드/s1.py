import sys
sys.stdin = open('input.txt')

T = int(input())
for num in range(1,T+1):
    N = int(input())
    arr = list(map(int, input()))
    C = [0] * 10

    for i in range(len(arr)):
        C[arr[i]] += 1


    for j in range(len(C)-1, -1, -1):
        if C[j] == max(C):
            max_cnt = C[j]
            max_value = j
            break

    print("#{} {} {}".format(num, max_value, max_cnt))
