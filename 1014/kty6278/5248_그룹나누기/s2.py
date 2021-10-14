import sys
sys.stdin = open('input.txt')

for tc in range(int(input())):
    n, m = map(int, input().split())
    person = list(map(int, input().split()))
    tree = [[] for _ in range(n+1)]
    for i in range(0, len(person), 2):
        my_list = [person[i], person[i+1]]
        tree[my_list[0]].append(my_list[1])
        tree[my_list[1]].append(0)
    cnt = -1
    print(tree)
    for tree_node in tree:
        if not tree_node:
            cnt += 1
        elif 0 not in tree_node:
            cnt += 1
    print('#{} {}'.format(tc+1, cnt))