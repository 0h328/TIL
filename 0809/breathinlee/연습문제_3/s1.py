import sys
sys.stdin = open('input.txt')


N = int(input())

for i in range(1, N+1):
    num = int(input())
    number_list = list(map(int, input(). split()))
    arr = [[0] * num for _ in range(num)]
    # numbers_list의 숫자만큼 0을 1로 바꿔줌
    for j in range(num):
        for k in range(number_list[j]):
            arr[j][k] = 1
    # print(arr)
    #
    cnt_list = []
    for a in range(num):
        for b in range(num):
            cnt = 0
            if arr[a][b] == 1:
                for m in range(a+1, num):
                    if arr[m][b] == 0:
                        cnt += 1
                        cnt_list.append(cnt)
    print('#{} {}'.format(i,max(cnt_list)))











