import sys
sys.stdin = open('input.txt')

def in_order(n):    # 중위 순회
    if n:
        in_order(left[n])   #왼쪽 자식노드부터 확인.
        visited.append(data[n][1])  # 본인 노드를 방문리스트에 담음
        in_order(right[n])  # 오른쪽 자식노드 확인.

for tc in range(1, 11):
    N = int(input())
    data = [[0]]    # 가장 처음 인덱스를 위해 [0]인 리스트 만들어줌.
    for i in range(N):
        data.append(list(input().split()))  # 각 정점정보들을 입력해줌
    left = [0] * (N+1)  # 노드의 갯수 만큼 왼쪽 오른쪽 자식정보를 담을 리스트 생성
    right = [0] * (N+1)
    for i in range(1, N+1):
        for j in range(2, 3):
            try:
                left[i] = int(data[i][j])   #왼쪽 오른쪽 리스트에 담음
                right[i] = int(data[i][j+1])
            except:
                pass

    visited = []    # 방문한 순서대로 입력하기 위함.
    in_order(1)
    print('#{} '.format(tc), *visited, sep='')
