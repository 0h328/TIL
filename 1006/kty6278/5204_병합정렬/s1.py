import sys
sys.stdin = open('input.txt')


def merge_sort(my_list):
    global cnt

    if len(my_list) < 2:                        # 1개일 때까지 분리
        return my_list
    mid = len(my_list) // 2                     # 2개 이상인 경우 mid값을 기준으로 양쪽으로 나눈다
    left = merge_sort(my_list[:mid])
    right = merge_sort(my_list[mid:])

    if left[-1] > right[-1]:                    # 나눠진 left와 right에서 왼쪽 오른쪽 마지막 값을 비교
        cnt += 1

    merge_list = []
    i = j = 0
    while i < len(left) and j < len(right):     # 현재 존재하는 left와 right를 비교해가면서 크기 비교를 통해 작은 것부터 merge_list에 담는다
        if left[i] < right[j]:
            merge_list.append(left[i])
            i += 1
        else:
            merge_list.append(right[j])
            j += 1
    merge_list += left[i:]                       # 다 비교하고도 남는 것들이 있으면 left,right순으로 합친다
    merge_list += right[j:]
    return merge_list

for tc in range(int(input())):
    n = int(input())
    my_list = list(map(int, input().split()))   #  받아온 수를 저장하는 리스트
    cnt = 0                                     # 마지막 수 비교하면서 왼쪽 마지막이 더 큰거 저장해주기 위한 변수

    result = merge_sort(my_list)[n//2]
    print('#{} {} {}'.format(tc+1, result, cnt))


