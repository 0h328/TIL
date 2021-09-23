import sys
sys.stdin = open('input.txt')

# 1 -> 2 -> 4 -> 8 -> 16 -> 8(p) -> 17 -> 8 -> 4(p) -> 9 -> 2(p) -> 5 -> 10 -> 5(p) -> 11 -> 2 -> 1(p)
# -> 3 -> 6 -> 12 -> 6(p) -> 13 -> 6 -> 3(p) -> 7 -> 14 -> 7(p) -> 15 -> 7 -> 3 -> 1
def in_order(num):                     # inorder(중위순회) 함수 만들기
    if num <= N:                       # 만약 num이 N보다 작을 때
        in_order(num*2)                # 재귀로 들어가기...
        print(node_list[num], end='')  # node_list의 num번째를 프린트, 기본값인 '\n'에서 ''으로 바꿔줘서 한 줄에 프린트
        in_order(num*2+1)              # 오른쪽 있나 체크


for tc in range(1, 11):
    N = int(input())
    node_list = [0] * (N + 1)          # index를 맞춰서 사용하고 싶어서 N + 1 해줌
    for i in range(N):
        node = list(input().split())
        node_list[i+1] = node[1]       # node의 글자를 node_list의 index에 맞게 넣어줌
    print('#{0}'.format(tc), end=' ')
    in_order(1)                        # 중위함수 1부터 시작
    print()
