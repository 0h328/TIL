import sys
sys.stdin = open('input.txt')

for T in range(10):
    dumps = int(input())
    boxes = list(map(int, input().split()))
    counting_list = [0] * 101
    min_idx, max_idx = 100, 0
    for b in boxes:
        max_idx = max(max_idx, b)
        min_idx = min(min_idx, b)
        counting_list[b] += 1

    while dumps:
        counting_list[max_idx]-=1
        counting_list[max_idx-1]+=1
        counting_list[min_idx]-=1
        counting_list[min_idx+1]+=1
        if counting_list[max_idx] == 0:
            max_idx-=1
        if counting_list[min_idx] == 0:
            min_idx+=1

        dumps-=1

    print('#{} {}'.format((T+1), max_idx-min_idx))

#1 13
#2 32
#3 54
#4 25
#5 87
#6 14
#7 39
#8 26
#9 13
#10 29
