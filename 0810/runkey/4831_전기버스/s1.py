import sys
sys.stdin = open("input.txt")

t = int(input()) # 노선 수
for tc in range(1, t + 1):
    k, n, m = map(int, input().split())
    # k : 한번 충전으로 최대한 이동할 수 있는 정류장 수
    # n : 종점인 N번 정류장
    # m : 충전기가 설치된 M개의 정류장
    charge_list = [0] * (n + 1)
    count = 0
    result = 0
    flag = 0

    for i in input().split():
        charge_list[int(i)] = 1     # 충전기가 설치된 주유소에 1을 채움

    while count <= n:
        if count > 0 and charge_list[count] == 1:
            result += 1

        max_idx = count + k if (count + k <= n) else n
        for j in range(max_idx, count - 1, -1):
            if j == count:
                flag = 1
                result = 0
                break

            if charge_list[j] == 1:
                count = count + j - 1
                result += 1
                break

        if flag == 1:
            break

    print("#{0} {1}".format(tc, result))