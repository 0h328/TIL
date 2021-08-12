import sys
sys.stdin = open('input.txt')

di = [0, 0, -1] # 좌, 우, 상
dj = [-1, 1, 0]

for _ in range(10):
    tc = int(input())
    arr = [list(map(int, input().split())) for _ in range(100)]
    print(arr)
    #2인 자리 찾는 거 검색
    i = 99
    for idx in range(100):
        if arr[99][idx] == 2:
            j = idx
            two_idx = idx
            break


    cnt = 0
    cnt_idx_l = 0
    cnt_idx_r = 0
    while cnt < 100:
        for k in range(2):
            n_i = i + di[k] #상하좌우 탐색용
            n_j = j + dj[k]

            if arr[n_i][n_j] == 1:  #k=0부터 시작, 왼쪽 1이면, cnt_idx += 1
                i = n_i             #k=1이면 오른쪽 탐색, 오른쪽 1이면
                j = n_j
                cnt_idx_l += (1-k)  #k=0이면 왼쪽인 경우니깐, left에 +1
                cnt_idx_r += k      #k=1이면 오른쪽인 경우니깐, right에 +1
            elif k == 0 and n_i == -1:
                continue
            else:                   #n_i, n_j
                n_i -= di[k]
                n_j -= dj[k]
        # 왼쪽&오른쪽 0이면, 위로 올라감, cnt += 1 (99까지 할 거임)
        i += di[2]
        j += dj[2]
        cnt += 1


    ans = two_idx - cnt_idx_l + cnt_idx_r

    print('#{} {}'.format(tc, ans))