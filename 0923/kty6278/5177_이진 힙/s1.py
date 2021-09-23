import heapq
import sys
sys.stdin = open('input.txt')

def solve(n):
    global cnt
    while n :
        n //= 2
        cnt += tree[n]

def heapify_sort(child):
    parent_node = child//2
    if parent_node < 0:
        return
    else:
        if tree[parent_node] > tree[child]:
            tree[child], tree[parent_node] = tree[parent_node], tree[child]
            heapify_sort(parent_node)

for tc in range(int(input())):
    n = int(input())
    node = list(map(int, input().split()))
    tree = [0]
    child = 1
    for no in node:
        tree.append(no)
        heapify_sort(child) # root 는 1
        child += 1

    #print(node)
    #heapq.heapify(node)                      # 부모 노드 < 자식 노드 자동으로 정렬 최소힙 만족
    #print(node)

    #print(tree)
    cnt = 0
    solve(n)
    print('#{} {}'.format(tc+1, cnt))