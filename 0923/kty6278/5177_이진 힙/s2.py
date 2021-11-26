import sys
sys.stdin = open('input.txt')
import heapq


for tc in range(int(input())):
    n = int(input())
    node = [0] + list(map(int, input().split()))

    #print(node)
    heapq.heapify(node)                      # 부모 노드 < 자식 노드 자동으로 정렬 최소힙 만족
    print(node)
    cnt = 0
    while n > 1:
        n //= 2
        cnt += node[n]
    print('#{} {}'.format(tc+1, cnt))