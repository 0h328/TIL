import sys
sys.stdin = open('input.txt')

def counting_sort(num):                     # 카운팅 정렬 함수
    cnt = [0] * max(num)
    for i in range(len(num)):
        cnt[num[i]-1] += 1
    for j in range(1, len(cnt)):
        cnt[j] += cnt[j-1]
    tmp = [0] * len(num)
    for k in range(len(num)-1, -1, -1):
        cnt[num[k]-1] -= 1
        tmp[cnt[num[k]-1]] = num[k]
    return tmp

for tc in range(1, 11):
    cnt = int(input())
    height = list(map(int, input().split()))

    while cnt:
        height = counting_sort(height)      # 카운팅 정렬로 정렬
        height[0] += 1                      # 최솟값 1 증가
        height[99] -= 1                     # 최댓값 1 감소
        cnt -= 1                            # 덤프 1회 감소

    height = counting_sort(height)          # 결과값 다시 정렬
    height_gap = height[99] - height[0]     # 최댓값과 최솟값 차이

    print('#{} {}'.format(tc, height_gap))
