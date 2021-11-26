import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    box = list(map(int, input().split()))
    max_val = 0
    for i in range(N-1):
        cnt = 0
        for j in range(i+1, N):
            if box[i] <= box[j]:
                cnt += 1
        drop = N - i - cnt - 1 # 전체 길이에서 i만큼 뺀것이 box[i]의 낙차이며 사이 공간이므로 -1을하고 i 이후 i보다 더 많은 불록개수를 가진 cnt를 빼면 총 낙차거리가나옴
        if max_val < drop:
            max_val = drop
    print(max_val)


"""
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
"""
# 이렇게 하면.. 전체 100*100이라는 조건을 줘야할텐데.......











