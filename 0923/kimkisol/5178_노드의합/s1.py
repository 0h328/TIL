import sys

sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T + 1):
    N, M, L = map(int, input().split())  # N: 노드 개수, M: 리프노드 개수, L: 출력할 노드 번호
    leaves = [list(map(int, input().split())) for _ in range(M)]
    result = 0

    # 리프 노드가 출력할 노드의 자식이면 결과값에 더하기
    for leaf in leaves:
        node, num = leaf[0], leaf[1]  # 노드번호, 노드의 숫자
        while node:  # 0보다 클 때
            node //= 2  # 2로 나눈 몫 대입
            if node == L:  # 이게 만약 출력 노드 번호와 같다면 자식인 것과 같음
                result += num  # 결과값에 노드 숫자 더하기
                break

    print('#{} {}'.format(t, result))
