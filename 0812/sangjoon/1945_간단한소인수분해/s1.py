import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    n = int(input())
    prime_nums = [2, 3, 5, 7, 11]  # 소수 리스트
    idx, cnt = 0, 0
    ans = []

    while idx < 5:

        if n % prime_nums[idx] == 0:  # 소수로 나누어질 경우 개수 추가
            n //= prime_nums[idx]
            cnt += 1

        else:
            ans.append(cnt)  # 해당 소수로 나눠지지 않을 경우, 다음 소수 탐색
            idx += 1
            cnt = 0

    print("#{} {}".format(test, " ".join(map(str, ans))))
