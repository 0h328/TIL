import sys
sys.stdin = open('input.txt')

def sub_tree(root):
    global cnt                                 # global 환경의 cnt를 받아옴
    if tree[root][0]:                          # 왼쪽 자식이 있을 때 cnt에 1 추가
        cnt += 1
        sub_tree(tree[root][0])                # 재귀함수 시작...
    if tree[root][1]:                          # 오른쪽 자식이 있을 때 cnt에 1 추가
        cnt += 1
        sub_tree(tree[root][1])

T = int(input())
for tc in range(1, T+1):
    E, V = map(int, input().split())           # 간선의 개수 E, 노드 V
    temp = list(map(int, input().split()))
    tree = [[0] * 3 for _ in range(E+2)]       # [왼쪽 자식, 오른쪽 자식, 부모]를 만들기 위함
    for i in range(E):
        parent, child = temp[i*2], temp[i*2+1]
        if not tree[parent][0]:                # 부모에 왼쪽 자식이 없을 때
            tree[parent][0] = child
        else:
            tree[parent][1] = child            # 왼쪽 자식이 있으면 오른쪽 자식에 저장
        tree[child][2] = parent                # 자식 노드의 index 2는 부모
    cnt = 1                                    # 처음 시작하는 노드도 개수에 포함 됨
    sub_tree(V)                                # 찾고자 하는 V를 sub_tree() 함수에 넣어 준다.
    print('#{0} {1}'.format(tc, cnt))