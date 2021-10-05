import sys
sys.stdin = open('input.txt')


asc = [[0, 0, 0, 0],  #0
       [0, 0, 0, 1],  #1
       [0, 0, 1, 0],  #2
       [0, 0, 1, 1],  #3
       [0, 1, 0, 0],  #4
       [0, 1, 0, 1],  #5
       [0, 1, 1, 0],  #6
       [0, 1, 1, 1],  #7
       [1, 0, 0, 0],  #8
       [1, 0, 0, 1],  #9
       [1, 0, 1, 0],  #A
       [1, 0, 1, 1],  #B
       [1, 1, 0, 0],  #C
       [1, 1, 0, 1],  #D
       [1, 1, 1, 0],  #E
       [1, 1, 1, 1]]  #F

code = [[[[[[[0 for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)] for _ in range(2)]

code[0][0][0][1][1][0][1] = 0
code[0][0][1][1][0][0][1] = 1
code[0][0][1][0][0][1][1] = 2
code[0][1][1][1][1][0][1] = 3
code[0][1][0][0][0][1][1] = 4
code[0][1][1][0][0][0][1] = 5
code[0][1][0][1][1][1][1] = 6
code[0][1][1][1][0][1][1] = 7
code[0][1][1][0][1][1][1] = 8
code[0][0][0][1][0][1][1] = 9

def pos_find(arr):
    for i in range(N):
        for j in range(M - 1, 5, -1):
            if arr[i][j] == 1:
                posi = i
                posj = j
                return posi, posj
T = int(input())

for tc in range(1,T+1):
    N, M = map(int, input().split())
    arr = [list(map(int, input())) for _ in range(N)]
    pos_i, pos_j = pos_find(arr)

    ans = []

    for i in range(8):
        x = code[arr[pos_i][pos_j-6]][arr[pos_i][pos_j-5]][arr[pos_i][pos_j-4]][arr[pos_i][pos_j-3]][arr[pos_i][pos_j-2]][arr[pos_i][pos_j-1]][arr[pos_i][pos_j]]
        ans.append(x)
        pos_j -= 7
    print(ans)
    ans = ans[::-1]
    print(ans)
    output = 0
    for i in range(0, 4):
        output += 3 * ans[2*i]
        output += ans[2*i + 1]


    if output%10:
        result = 0
    else:
        result = sum(ans)
    print('#{} {}'.format(tc, result))


# is_break = False라는 변수 적어놓고
# 안쪽 for문 안에서 if문 안에 True로 바꾸고
# 바깥쪽 for문 안에서 if문 False? 되면 break 걸기