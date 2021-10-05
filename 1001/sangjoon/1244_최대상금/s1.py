# 문제 푼 시간
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def dfs(cnt, idx):

    if not cnt:  # 모든 교환이 끝난 경우
        tmp = int("".join(map(str, n)))
        ans[0] = max(ans[0], tmp)
        return

    if n == sn:  # 최대값을 완셩한 경우
        if chk:  # 중복값이 있을경우
            tmp = int("".join(map(str, n)))
        else:
            if cnt % 2:
                n[-1], n[-2] = n[-2], n[-1]
                tmp = int("".join(map(str, n)))
                n[-1], n[-2] = n[-2], n[-1]
                ans[0] = max(ans[0], tmp)
            else:
                tmp = int("".join(map(str, n)))
        ans[0] = max(ans[0], tmp)
        return

    for i in range(idx, l):
        if n[i] == sn[idx]:
            if i == idx:  # 기존 위치가 최대값인 경우
                dfs(cnt, idx+1)
            else:
                n[idx], n[i] = n[i], n[idx]
                dfs(cnt-1, idx+1)
                n[idx], n[i] = n[i], n[idx]


test_case = int(input())

for test in range(1, test_case + 1):
    n, c = map(int, input().split())
    n = list(map(int, list(str(n))))
    l = len(n)
    ans = [0]
    sn = sorted(n, reverse=True)  # 최대값 생성
    chk = False  # 중복숫자 판별
    for num in sn:
        if sn.count(num) > 1:
            chk = True

    dfs(c, 0)

    print("#{} {}".format(test, ans[0]))
