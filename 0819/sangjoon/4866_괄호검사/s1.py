# 문제 푼 시간
# 풀이법: 스택/딕셔너리로 구현
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def check_bracket(string: str):
    stack = []
    bracket_dict = {"(": ")", "{": "}"}  # 브라캣 짝연결

    for i in range(len(string)):  # 모든 문자 순회
        letter = string[i]

        if letter in bracket_dict.keys():  # 여는 괄호일 경우
            stack.append(letter)

        elif letter in bracket_dict.values():  # 닫는 괄호일 경우
            if not stack:  # 앞에 여는 괄호가 없을 경우
                return 0

            if bracket_dict[stack[-1]] == letter:  # 짝이 맞을 경우
                stack.pop()
            else:  # 선행되는 괄호 짝이 안 맞을 경우
                return 0

    if stack:  # 여는 괄호가 남았을 경우
        return 0

    return 1


test_case = int(input())

for test in range(1, test_case + 1):
    string = input()
    print("#{} {}".format(test, check_bracket(string)))
