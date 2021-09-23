import sys
sys.stdin = open('input.txt')

def find_node(num):                                # find_node() 함수 생성
    # global result                                # global로 result를 받아옴
    if num > N:                                    # 이 부분이 없으면 out_of_range 오류가 납니다.
        return 0                                   # (노드의 개수를 넘지 않을 때까지만 재귀가 돈다는 뜻)
    if tree[num]:                                  # 이 부분이 없으면 답이 그냥 0만 나옵니다. => 왜냐하면 리프 노드를 생각해줘야하기 때문 뚜둥
        return tree[num]                           # (tree의 num번째에 숫자가 있으면 그냥 그 수를 return)
    left = num * 2                                 # 왼쪽 노드
    right = num * 2 + 1                            # 오른쪽 노드
    tree[num] = find_node(left) + find_node(right) # result를 찾아라 오바.
    return tree[num]                               # 찾았으면 리턴 오바.

T = int(input())
for tc in range(1, T+1):
    N, M, L = map(int, input().split())            # 노드의 개수 N, 리프 노드의 개수 M, 노드 번호 L
    tree = [0 for _ in range(N+1)]
    for i in range(M):                             # 리프 노드의 개수만큼 반복문을 돌려서 tree에 저장
        node, node_num = map(int, input().split())
        tree[node] = node_num
    # print(tree)
    # result = 0                                   # result를 0으로 저장
    find_node(L)                                   # find_node() 함수에 값을 출력할 노드 L값을 넣어 찾기
    print('#{0} {1}'.format(tc, find_node(L)))