import sys

sys.stdin = open('input.txt')


def merge_sort(data):
    if len(data) <= 1:
        return data

    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right) # 전체 정렬 데이터 만들기


def merge(left, right):
    global cnt

    ln, rn = len(left), len(right) # 왼쪽 길이, 오른쪽 길이
    result = [0] * (ln + rn) # 새롭게 만들 결과값은 두 길이의 합
    li, ri, i = 0, 0, 0 # 인덱스를 오른쪽 왼쪽 일반으로 구분
    if left[-1] > right[-1]: # 가장 뒤의 원소가 왼쪽이 더 큰 경우는 카운트
        cnt += 1

    while li != ln and ri != rn: # 둘다 순회를 마치지 않은 경우
        if left[li] <= right[ri]: # 고정된 오른쪽을 기준으로 만약 왼쪽 수가 더 작다면
            result[i] = left[li] # 해당하는 인덱스의 결과값에 넣어준다
            i += 1 # 인덱스 증가와
            li += 1 # 왼쪽 인덱스도 역시 증가
        else: # 왼쪽 수가 더 작은 경우가 없다면 그 자리는 오른쪽 해당 인덱스의 몫
            result[i] = right[ri]  # 값을 넣어주고
            i += 1 # 인덱스와
            ri += 1 # 오른쪽 인덱스 증가

    # 끝났는데 혹시라도 다 돌지 않은 경우
    if li != ln: # 왼쪽이 남은 경우
        while li != ln:
            result[i] = left[li]
            i += 1
            li += 1

    if ri != rn: # 오른쪽이 남은 경우
        while ri != rn:
            result[i] = right[ri]
            i += 1
            ri += 1

    return result # 정렬된 데이터를 반환


for test in range(1, 1 + int(input())):
    N = int(input())
    data = list(map(int, input().split()))
    cnt = 0

    data = merge_sort(data)
    answer = data[N // 2] # 가운뎃 값값
   print('#{} {} {}'.format(test, answer, cnt))
