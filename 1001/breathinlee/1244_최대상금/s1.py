import sys
sys.stdin = open('input.txt')

# 미완성
# numpad는 int, 최대 6자리 / exchange는 최대 10번

T = int(input())
for tc in range(1, T+1):
    numpad, exchange = input().split()
    exchange = int(exchange)
    num_list = []
    for number in numpad:
        num_list.append(int(number))
    visited = [0] * len(num_list)
    max_value = max(num_list)
    max_idx = num_list.index(max_value)
    cnt = num_list.count(max_value)
    maxV = 0

    if cnt == 1:
        num_list[0], num_list[max_idx] = num_list[max_idx], num_list[0]
        maxV = int(''.join(num_list))
    else:
        idx = 0
        while exchange > 0:
            if num_list[idx] < max_value:
                num_list[idx], num_list[max_idx] = num_list[max_idx], num_list[idx]
                idx += 1
                exchange -= 1

