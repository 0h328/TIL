import sys
sys.stdin = open("input.txt")

N = int(input())
for i in range(1, N+1):
    num = int(input())
    num_list = list(map(int, input(). split()))
    for j in range(num - 1, 0, -1):               # num_list를 오름차순으로 정렬하기 위함
        for k in range(0, j):                     # 1번 시행하면 가장 큰 값이 가장 오른쪽에 위치 => index를 하나씩 줄여가며 반복
            if num_list[k] > num_list[k + 1]:
                num_list[k], num_list[k + 1] = num_list[k + 1], num_list[k]
    max_num = num_list[num - 1]                   # 오름차순으로 정렬했으므로 가장 오른쪽 값이 max
    min_num = num_list[0]                         # 첫 번째 index가 min
    print('#{} {}'.format(i, max_num - min_num))
    # print(num_list)
