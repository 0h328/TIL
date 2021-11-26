#3. sol
# 4조 final solution

import sys
sys.stdin = open('input.txt')

T = int(input())

for idx in range(1, T + 1):                         # From sol1
    n = int(input())
    numbers = input()
    cnt = [0] * 10
    for number in numbers:
        cnt[int(number)] += 1

		max_idx = 0                                     # From sol2
    for i in range(1, 10):
        if cnt[max_idx] <= cnt[i]:
            max_idx = i

    print('#{} {} {}'.format(idx, max_idx, cnt[max_idx]))