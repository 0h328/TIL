'''
1. 입력 받은 블럭 높이 리스트를 정렬한다.
2. 각 끝의 인덱스의 값들을 빼고 추가한다. 덤프 횟수를 1씩 뺀다
3. 다시 정렬을 실시한다.
4. 남은 덤프 횟수만큼 반복
5. max 값과 min 값 비교하여 높이차이를 구한다.


* 예상 시간 복잡도 O(N^3) or O(N^2logN)
남은 덤프만큼 반복 O(N)
   정렬 O(N^2) or O(NlogN)
-> 시간 복잡도 줄이는 방안을 생각해볼 필요 있어보임
'''

import sys
sys.stdin = open('input.txt')


for tc in range(1, 11):
    dump_remain = int(input())                          # 남은 이동횟수
    num_list = list(map(int, input().split()))          # 블럭 높이 리스트

    while dump_remain:                                  # dump 남은 횟수만큼 반복
        num_list.sort()                                 # 높이 정렬

        num_list[0] += 1                                # 가장 낮은 높이 + 1
        num_list[-1] -= 1                               # 가장 높은 높이 - 1
        dump_remain -= 1                                # dump 횟수 - 1

    num_list.sort()                                     # 마지막 작업 이후 정렬
    answer = num_list[-1] - num_list[0]                 # 제일 높은 높이 - 제일 낮은 높이

    print('#{} {}'.format(tc, answer))