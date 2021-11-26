# like 중위순회?!

def make_binary_tree(num):
    global value
    if num <= N:                        # N개 까지만 조사
        make_binary_tree(num * 2)       # 왼자식
        tree[num] = value               # 값 넣어주고
        value += 1                      # 그다음 값 진행
        make_binary_tree(num * 2 + 1)   # 오른자식

import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    tree = [0] * (N+1)                  # 인덱스처럼 사용 / 해당 위치 값

    value = 1                           # 값 시작이 1 (~N까지)
    make_binary_tree(1)                 # 완전 이진 트리 노드 번호!
    print('#{} {} {}'.format(tc, tree[1], tree[N//2]))

'''
N이 주어졌을 때 완전 이진 트리로 만든 이진 탐색 트리의 루트에 저장된 값과, N/2번 노드(N이 홀수인 경우 소수점 버림)에 저장된 값을 출력하는 프로그램을 만드시오.
6
8
15

#1 4 6
#2 5 2
#3 8 14
'''