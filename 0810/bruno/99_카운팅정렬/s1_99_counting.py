import sys
sys.stdin = open('input.txt')

num = list(map(int, input().split()))

def counting_sort(num):
    cnt = [0] * max(num)                    # 리스트의 숫자 범위만큼 0으로 된 리스트 생성

    for i in range(len(num)):               # 각 숫자들의 갯수를 담은 리스트 생성
        cnt[num[i]-1] += 1                  # 각 숫자가 발견될 때마다 1씩 증가

    for j in range(1, len(cnt)):            # cnt 리스트의 값을 누적으로 변경
        cnt[j] += cnt[j-1]                  # 앞의 숫자와 더해 뒷요소에 저장

    tmp = [0] * len(num)                    # 정렬된 숫자가 담길 새 리스트 생성
    for k in range(len(num)-1, -1, -1):     # 기존 리스트의 뒤에서부터 카운트하며
        cnt[num[k]-1] -= 1                  # 해당 숫자의 갯수를 cnt 리스트에서 차감
        tmp[cnt[num[k]-1]] = num[k]         # tmp 리스트에 해당 숫자 위치 저장
    return tmp



print(counting_sort(num))
