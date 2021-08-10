import sys
sys.stdin = open('input.txt')

for idx in range(1, 11):
    N = int(input())
    num = list(map(int, input().split()))

    result = 0
    for j in range(2, len(num)-2):
        max_num = max(num[j+1], num[j+2], num[j-1], num[j-2])
        if (num[j] < max_num):
            continue
        else:
           result += (num[j]-max_num)

    print('#{0} {1}'.format(idx, result))



