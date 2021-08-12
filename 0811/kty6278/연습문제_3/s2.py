# input 데이터를 불러온다.
import sys
sys.stdin = open('input.txt')

arr = list(map(int, input().split()))

# 비트 연산자 사용
num = len(arr)

for i in range(1 << num):
    num_arr = 0
    for j in range(num + 1):
        if i & (1 << j):
            print(arr[j], end = ' ')

    # if num_arr == 10:
        # print('vvv')
    # else:
        # print()
    print()