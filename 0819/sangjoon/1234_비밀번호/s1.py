# 문제 푼 시간
# 풀이법: 스택 구현
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def get_password(word: str):
    password = list(word)
    stack = []

    while True:  # 변경사항이 없을 때까지 무한반복
        check = False

        for num in password:
            if stack and num == stack[-1]:  # 중복제거
                stack.pop()
                check = True
            else:
                stack.append(num)

        password, stack = stack, []

        if check:  # 변경사항이 없을 경우
            break

    return "".join(password)


test_case = 10

for test in range(1, test_case + 1):
    n, string = input().split()
    ans = get_password(string)
    print("#{} {}".format(test, ans))
