import sys
sys.stdin = open('input.txt')

M = int(input())
N = int(input())
perfect_square_num = []

# case 1
for i in range(M, N+1):
    tmp = i**0.5
    if int(tmp) == tmp:
        perfect_square_num.append(i)

if perfect_square_num:
    print(sum(perfect_square_num))
    print(min(perfect_square_num))
else:
    print(-1)

# case 2
# tmp = 1
# while tmp**2 <= N:
#     if M <= tmp**2 <= N:
#         perfect_square_num.append(tmp**2)
#     tmp += 1
#
# if len(perfect_square_num) == 0:
#     print(-1)
# else:
#     print(sum(perfect_square_num))
#     print(min(perfect_square_num))