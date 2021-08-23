# 재귀
# 웹엑스 시간에 배운내용을 하나하나 파헤쳐가면서 이해할려고 했지만 이해를 못한 관계로
# 배운 내용으로 복붙했고, 도착지점 확인 코드만 추가작성하였다.
# 결론 : 풀었지만 푼게아니다.

def dfs(s):                                             # 매개변수를 s와 e 2개를 안줘도 출력 가능하구나
    visited[s] = 1
    for w in range(100):                                # 시작이 0부터니까 범위를 0부터 하면됨.
        if G[s][w] == 1 and not visited[w]:             # 그래프의 노드가 1이고, visited가 0이면
            dfs(w)                                      # 돌아가라

    if visited[e]:                                      # visited에 도착지가 체크되어있으면
        return 1                                        # 1 반환

    return 0                                            # 아니면 0 반환

import sys
sys.stdin = open('input.txt')

T = 10
for tc in range(1, T+1):
    N, E = map(int, input().split())
    temp = list(map(int, input().split()))

    G = [[0 for _ in range(100)] for _ in range(100)]

    for i in range(E):
        G[temp[i*2]][temp[i*2+1]] = 1                   # 단방향이므로 이것만 작성해도 됨.

    visited = [0] * 100                                 # 99로 고정했으니 길이는 100으로 정하기.

    s = 0
    e = 99

    print('#{} {}'.format(tc, dfs(s)))