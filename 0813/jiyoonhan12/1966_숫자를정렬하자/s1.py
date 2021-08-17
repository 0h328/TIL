import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
    num = int(input())
    num_list = list(map(int, input().split()))
    num_list.sort()
    print('#{}'.format(t), end=' ')
    for n in range(num):
        print('{}'.format(num_list[n]), end=' ')
    print()