import sys
sys.stdin = open('input.txt')

num = int(input())
for T in range(1, num+1):
    N, M = map(int, input().split())


























    # row_find_list = [input() for _ in range(N)]
    # # print(row_find_list)
    # col_find_list = list(zip(*row_find_list))
    # # print(col_find_list)
    #
    # palindrome_list = []
    #
    # for i in range(N):
    #     for j in range(N-M+1):
    #         if row_find_list[i][j:j+M] == row_find_list[i][j:j+M][::-1]:
    #             palindrome_list.append(row_find_list[i])
    #
    # for i in range(N):
    #     for j in range(N-M+1):
    #         if col_find_list[i][j:j+M] == col_find_list[i][j:j+M][::-1]:
    #             palindrome_list.append(''.join(row_find_list[i]))
    #
    # print('#{} {}'.format(T, *palindrome_list))

    # for i in range(x):
    #     my_str = ''
    #     result = ''
    #     for j in range(y):
    #         my_str += find_list[j][i]
    #         if my_str[0:x//2] == my_str[-1:-(x//2+1):-1]:
    #             result = my_str
    #         else:
    #             result = False
    #
    # print('#{0} {1}'.format(T, result))

            # for j in range(x):
            #     my_str += find_list[i][0][j]
            # print(my_str)
                # if find_list[i][0][0:y//2] == find_list[i][0][-1:-(y//2+1):-1]:


    # for j in range(y):
    #     if find_list[j][0] == find_list
