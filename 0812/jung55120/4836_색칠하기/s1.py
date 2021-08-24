import sys
sys.stdin = open('input.txt')

num = int(input())
for T in range(1, num+1):
    cnt = int(input())
    point_list = [[0] * 10 for _ in range(10)]
    # print(point_list)
    for _ in range(cnt):
        r1, c1, r2, c2, color = map(int, input().split())

        for i in range(r1, r2+1):
            for j in range(c1, c2+1):
                point_list[i][j] += color

    count_num = 0

    for k in range(10):
        for l in range(10):
            if point_list[k][l] > 2 :
                count_num +=1


    print('#{} {}'.format(T,count_num))

# [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 1, 1, 1, 0, 0, 0, 0, 0],
#  [0, 0, 1, 3, 3, 2, 2, 0, 0, 0],
#  [0, 0, 1, 3, 3, 2, 2, 0, 0, 0],
#  [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
#  [0, 0, 0, 2, 2, 2, 2, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
#  [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]

