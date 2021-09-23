import sys

sys.stdin = open('input.txt')


def DFS(index):
    global cnt # 글로벌로 관리
    cnt += 1
    for i in tree[index]:
        DFS(i)


for test in range(1, 1 + int(input())):
    E, N = map(int, input().split())
    data = list(map(int, input().split()))
    tree = [[] for _ in range(E + 2)]

    for i in range(0, E * 2, 2): # 최대 갯수를 2개씩 건너뛰면서
        a = int(data[i]) # 인덱스
        b = int(data[i + 1]) # 해당 값

        tree[a].append(b)
    cnt = 0
    answer = DFS(N)

    print('#{} {}'.format(test,cnt))
