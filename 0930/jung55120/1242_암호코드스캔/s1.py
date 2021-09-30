# import sys
# sys.stdin = open('input.txt')
#
# asc = [[0, 0, 0, 0],  #0
#        [0, 0, 0, 1],  #1
#        [0, 0, 1, 0],  #2
#        [0, 0, 1, 1],  #3
#        [0, 1, 0, 0],  #4
#        [0, 1, 0, 1],  #5
#        [0, 1, 1, 0],  #6
#        [0, 1, 1, 1],  #7
#        [1, 0, 0, 0],  #8
#        [1, 0, 0, 1],  #9
#        [1, 0, 1, 0],  #A
#        [1, 0, 1, 1],  #B
#        [1, 1, 0, 0],  #C
#        [1, 1, 0, 1],  #D
#        [1, 1, 1, 0],  #E
#        [1, 1, 1, 1]]  #F
#
# def ascii_to_hex(c):
#     # 9 이하
#     if c <= '9':
#         return ord(c) - ord('0')
#     # 10 이상
#     else:
#         return ord(c) - ord('A') + 10
#
# def hex_to_binary(x):
#     global pos
#     for i in range(4):
#         t.append(asc[x][i])
#
# T = int(input())
# for tc in range(1, T+1):
    # N, M = map(int, input().split())
    # arr = [input() for _ in range(N)]
#     pos = -1
#     t = []
#     find_list = []
#     for i in range(N):
#         for j in range(M-1, -1, -1):
#             if arr[i][j] != '0':
#                 find_list.append(arr[i][:j+1])
#                 break
#             continue
#     amho_list = list(set(find_list))
#
#     for i in range(len(amho_list)):
#         for j in amho_list[i]:
#             hex_to_binary(ascii_to_hex(j))
#
#
#     new_t = t[len(t)-56:len(t)]
#     print(amho_list)
#     print(new_t)
