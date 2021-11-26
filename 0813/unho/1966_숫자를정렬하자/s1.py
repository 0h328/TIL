import sys
sys.stdin = open('input.txt')



test_case = int(input())

for tc in range(1, test_case+1):
    num = int(input())
    num_list = list(map(int, input().split()))

    num_list.sort()

    print('#{} '.format(tc), end='')
    print(*num_list)