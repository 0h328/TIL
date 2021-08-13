import sys
sys.stdin = open('input.txt')

N = int(input())

arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]

for tc in range(1, N+1):
    a, b = list(map(int, input().split()))
    ans = 0
    #10000000101 이런 경우, 각 자리수 합이 3이 되는 경우, 그 값이 1일 때, 그 인덱스 해당 값 더하기
    for i in range(1, 1 << 12):
        new_arr = []
        for j in range(12):
            if i & (1 << j):
                new_arr.append(arr[j])
        if len(new_arr) == a and sum(new_arr) == b:
            ans += 1
    print('#{} {}'.format(tc, ans))
