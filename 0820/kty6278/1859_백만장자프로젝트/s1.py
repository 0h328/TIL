import sys
sys.stdin = open('input.txt')

T = int(input())
for t in range(1, T + 1):
    N = int(input())
    nums = list(map(int, input().split()))
    new_list = nums[::-1]
    max_value = new_list[0]
    total = 0
    for i in range(1, len(new_list)):
        if max_value <= new_list[i]:
            max_value = new_list[i]
        else:
            total += (max_value - new_list[i])
    print(f'#{t} {total}')
