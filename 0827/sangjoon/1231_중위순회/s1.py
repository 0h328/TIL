# 문제 푼 시간
# 풀이법: 중위 순회
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def in_order(node: str):  # 중위 순회
    global ans

    if tr[node][1]:
        in_order(tr[node][1])

    ans += tr[node][0]

    if tr[node][2]:
        in_order(tr[node][2])


test_case = 10

for test in range(1, test_case + 1):
    n = int(input())

    tr = {str(i): ["", 0, 0] for i in range(1, n + 1)}  # 트리 초기화:  문자 및 자식 순 저장

    for _ in range(n):  # 트리 생성
        lst = list(input().split())
        parent = lst.pop(0)
        for i in range(len(lst)):
            tr[parent][i] = lst[i]

    ans = ""  # 정답초기화
    in_order("1")

    print("#{} {}".format(test, ans))