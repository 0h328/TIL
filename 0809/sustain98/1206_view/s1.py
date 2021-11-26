import sys
sys.stdin = open('input.txt')

for t in range(1, 11):
    res = 0
    num = int(input())
    l = list(map(int, input().split()))
    for i in range(2, num-2):
        max_height = max(l[i-2], l[i-1], l[i+1], l[i+2])
        if max_height < l[i]:
            res += l[i] - max_height
    print('#{0} {1}'.format(t, res))


# for t in range(1, 11):
#     res = 0
#     num = int(input())
#     l = list(map(int, input().split()))
#     max_list = [0] + [max(l[i], l[i-1]) for i in range(1,num)]
#     for i in range(2, num-2):
#         max_height = max(max_list[i-1], max_list[i+2])
#         if max_height < l[i]:
#             res += l[i] - max_height
#     print('#{0} {1}'.format(t, res))


