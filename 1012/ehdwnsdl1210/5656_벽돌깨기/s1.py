import sys
sys.stdin = open('input.txt')

T = int(input())

for tc in range(1, T+1):
    N, W, H = map(int, input().split())                             # 횟수, 가로, 세로
    brick = [list(map(int, input().split())) for _ in range(H)]     # 0은 빈공간, 나머진 있는 곳
    # print(brick)                                                  # 배열 회전은 정사각형만?!

    # 첫행 순회하면서, DFS 들어감
    # 열이 선택되고, 0이면 다음행으로 계속들어감
    # 이제 숫자가 나오면 BFS 돌림(1개씩)
    # 돌면서 0으로 바꿔주면 되긴하는데... 어떻게 중력을 구현?!


'''
#1 12
#2 27
#3 4
#4 8
#5 0
'''