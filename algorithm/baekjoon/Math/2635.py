# import copy
# import time
# start = time.time()

N = int(input())

a_res = []
a_len = 0

for k in range(N+1):
    a = [N, k]

    while True:
        if a[-2] - a[-1] >= 0:
            a.append(a[-2] - a[-1])
        else:
            break

    if a_len < len(a):
        a_len = len(a)
        a_res = a[:]

print(a_len)
print(*a_res)

# print(time.time() - start)
# 2.315953254699707

# N = int(input())
#
# a_res = []
#
# for k in range(N+1):
#     a = [N, k]
#     while a[-2] - a[-1] >= 0:
#         a.append(a[-2] - a[-1])
#     a_res.append(a)
#
# max_len = len(a_res[0])
# for i in a_res:
#     if max_len < len(i):
#         max_len = len(i)
#     if max_len == len(i):
#         ans = i
#
# print(max_len)
# print(*ans)