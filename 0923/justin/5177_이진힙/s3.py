def insert(value):
    heap.append(value)                                                                   # 일단 append (마지막 요소로 추가됨)
    now_index = len(heap) - 1                                                            # 마지막 인덱스
    while now_index > 0:                                                                 # 부모의 인덱스 : last_index // 2
        parent_index = now_index // 2
        if heap[parent_index] > heap[now_index]:                                         # 부모의 값과 비교해서 추가된 값이 작다면?
            heap[parent_index], heap[now_index] = heap[now_index], heap[parent_index]    # 자리 바꾸기
        now_index = now_index // 2

def get_result_sum():
    result = 0
    now_index = len(heap) - 1
    while now_index > 0:
        now_index = now_index // 2
        result += heap[now_index]
    return result

import sys
sys.stdin = open('input.txt')
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    temp = list(map(int, input().split()))
    heap = [0]
    for number in temp:
        insert(number)
    print('#{} {}'.format(tc, get_result_sum()))
