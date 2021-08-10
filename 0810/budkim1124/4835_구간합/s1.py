import sys
sys.stdin = open('input.txt')

T = int(input())
for num in range(1,T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))

    max_li = 0
    min_li = 10001*M
    for idx in range(M, N+1):
        sum_list = sum(arr[idx-M:idx])

        if max_li < sum_list:
            max_li = sum_list

        if min_li > sum_list:
            min_li = sum_list

    print("#{} {}".format(num, max_li-min_li))








# 문제 이해 제대로 못해서 틀림

# T = int(input())
# for num in range(1,T+1):
#     [N, M] = list(map(int, input().split()))
#     arr = list(map(int, input().split()))
#
#
#     max_result = 0
#     tmp_arr = arr[:]
#     for _ in range(M):
#         my_max = min(tmp_arr)
#
#         for i in range(len(tmp_arr)):
#             if my_max < tmp_arr[i]:
#                 my_max = tmp_arr[i]
#         max_result += my_max
#
#         tmp_arr.remove(my_max)
#
#
#     min_result = 0
#     tmp_arr = arr[:]
#     for _ in range(M):
#         my_min = max(tmp_arr)
#
#         for i in range(len(tmp_arr)):
#             if my_min > tmp_arr[i]:
#                 my_min = tmp_arr[i]
#         min_result += my_min
#
#         tmp_arr.remove(my_min)
#
#     print("#{} {}".format(num, max_result - min_result))





