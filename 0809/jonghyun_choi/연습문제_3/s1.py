import sys
sys.stdin = open('input.txt')

N = int(input())

for num in range(N):
    m = int(input())
    box_list = list(map(int,input().split()))
    cnt_list = [0]* (m+1)
    for i in range(len(box_list)):
        for j in range(i+1, len(box_list)):
            if box_list[i] > box_list[j]:
                cnt_list[i+1] += 1
    max_value = max(cnt_list)

    print('#{} {}'.format(num+1,max_value))
