import sys
sys.stdin = open('input.txt')
# 식까지는 만들었고, stack으로 풀어보고 싶었는데 해결이 안됐다..
# 어떻게 해야할까? 고민해보자.
def in_order(num):                     # inorder(중위순회) 함수 만들기
    global str_num
    if num <= N:                      # 만약 num이 N보다 작을 때
        if node_list[num] in ('+', '-', '*', '/'):
            str_num += '('
            in_order(num*2)                # 재귀로 들어가기...
            str_num += node_list[num]
            in_order(num * 2 + 1)  # 오른쪽 있나 체크
            str_num += ')'
        else:
            in_order(num*2)                # 재귀로 들어가기...
            str_num += node_list[num]
            in_order(num * 2 + 1)  # 오른쪽 있나 체크
    return str_num

for tc in range(1, 11):
    N = int(input())
    node_list = [0 for _ in range(N+1)]         # index를 맞춰서 사용하고 싶어서 N + 1 해줌

    for i in range(N):
        node = list(input().split())
        node_list[i+1] = node[1]
    # print(node_list)
    str_num = ''
    print(in_order(1))                        # 중위함수 1부터 시작
    # print(str_num)
    # print(eval(str_num))


