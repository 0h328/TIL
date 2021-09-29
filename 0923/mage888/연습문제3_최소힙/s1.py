# 최소힙 - 라이브러리 활용(최소힙이 기본)
# import heapq
# heap = [7, 2, 5, 3, 4, 6]
#
# print(*heap)                        # 7 2 5 3 4 6
# heapq.heapify(heap)
# print(*heap)                        # 2 3 5 7 4 6
# heapq.heappush(heap, 1)
# print(*heap)                        # 1 3 2 7 4 6 5
# heapq.heappush(heap, 8)
# print(*heap)                        # 1 3 2 7 4 6 5 8
# heapq.heappush(heap, 12)
# print(*heap)                        # 1 3 2 7 4 6 5 8 12
# heapq.heappop(heap)
# print(*heap)                        # 2 3 5 7 4 6 12 8
# heapq.heappop(heap)
# print(*heap)                        # 3 4 5 7 8 6 12
# heapq.heappop(heap)
# print(*heap)                        # 4 7 5 12 8 6
#
# print('--------------------------')
# while heap:                              # 오름차순 정렬
#     print(heapq.heappop(heap), end=' ')  # 4 5 6 7 8 12
# print()
# print('--------------------------')
#
# ###########################################################
# # 최대힙
# my_heap = [7, 2, 5, 3, 4, 6]
# heap2 = []
# for i in range(len(my_heap)):
#     # tuple -> 첫 번째 값을 기준으로 heap 구성 -> 오름차순
#     # 2번째 원소는 자연스럽게 내림차순 정렬
#     heapq.heappush(heap2, (-my_heap[i], my_heap[i]))
# print(heap2)
#
# # 내림차순 정렬
# while heap2:
#     # 2번째 원소만 뽑자
#     # print(heapq.heappop(heap2)[0], end=' ') # -7 -6 -5 -4 -3 -2
#     print(heapq.heappop(heap2)[1], end=' ')  # 7 6 5 4 3 2 1

import heapq
heap = []
heapq.heappush(heap, 7)
heapq.heappush(heap, 5)
heapq.heappush(heap, 6)
heapq.heappush(heap, 8)
heapq.heappush(heap, 3)
heapq.heappush(heap, 1)





print(heap)