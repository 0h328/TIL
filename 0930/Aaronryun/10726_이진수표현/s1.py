import sys

sys.stdin = open('input.txt')

#
# for test in range(1, 1 + int(input())):
#     N, M = map(int, input().split())
#
#     data = format(M, 'b')
#
#     if '1'*N == data[-N:]:
#         print('#{} ON'.format(test))
#     else:
#         print('#{} OFF'.format(test))

ans = []
for test in range(1, int(input()) + 1):
    N, M = map(int, input().split())

    if bin(M)[-N:]=='1'*N:
        ans.append('#{} ON'.format(test))
    else:
        ans.append('#{} OFF'.format(test))
print('\n'.join(ans))