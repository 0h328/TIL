'''
두개를 쌍으로 이루어서 리스트 오른쪽 끝까지 순환
두 값을 비교하여 큰 수를 오른쪽으로 옮김
1번 순환하면 다시 처음부터 반복

시간 복잡도 O(n^2)
'''

import sys
sys.stdin = open('input.txt')


def bubble_sort(li):                                    # 버블 정렬 함수
    for i in range(len(li) - 1, -1, -1):                # 한번 순환시마다 오른쪽에 한번씩 덜 순환해도 됨
        for j in range(0, i):                           # 0번 인덱스부터 i인덱스 이전까지 순환
            if li[j] > li[j + 1]:                       # 오른쪽 값이 더 크면 값 교환
                li[j], li[j + 1] = li[j + 1], li[j]

    return li


num_list = list(map(int, input().split()))
sorted_list = bubble_sort(num_list)

print(sorted_list)