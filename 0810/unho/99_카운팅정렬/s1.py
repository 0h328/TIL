'''
1. 각 요소들이 몇번 나오는지 갯수를 세어서 새로운 리스트에 저장
2. 갯수를 누적합으로 저장
3. 정렬할 리스트의 제일 뒤에 값부터 누적합의 수 - 1 의 인덱스에 값 저장하고, 누적합은 -1
'''

import sys
sys.stdin = open('input.txt')

def counting_sort(li):
    sorted_list = [0] * len(li)                     # 정렬된 리스트를 담을 변수
    max_value = li[0]                               # 리스트에서 최고값을 찾음
    min_value = li[0]                               # 리스트에서 최솟값을 찾음

    for n in li:
        if max_value < n:
            max_value = n
        elif min_value > n:
            min_value = n

    cnt_list = [0] * (max_value + 1 - min_value)        # 리스트에서 최고값의 크기 + 1 리스트 생성

    for n in li:                                        # 해당 숫자의 갯수를 세어서 리스트에 저장
        cnt_list[n - min_value] += 1

    for idx in range(1, len(cnt_list)):                 # 누적합으로 저장
        cnt_list[idx] = cnt_list[idx-1] + cnt_list[idx]

    for n in li:                                        # 새로운 리스트에 정렬된 리스트 저장
        sorted_list[cnt_list[n-min_value]-1] = n
        cnt_list[n-min_value] -= 1

    return sorted_list

num_list = list(map(int, input().split()))
sorted_list = counting_sort(num_list)

print(sorted_list)