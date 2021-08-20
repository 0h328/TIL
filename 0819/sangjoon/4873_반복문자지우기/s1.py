# 문제 푼 시간
# 풀이법: 스택/딕셔너리로 구현
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())

for test in range(1, test_case + 1):
    word = input()
    stack = []
    for letter in word:
        if not stack:
            stack.append(letter)
            continue
        if letter == stack[-1]:
            stack.pop()
        else:
            stack.append(letter)

    print("#{} {}".format(test, len(stack)))