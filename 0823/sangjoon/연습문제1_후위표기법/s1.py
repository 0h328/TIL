# 문제 푼 시간
# 풀이법: Count 사용
import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def get_postfix(prefix: str):
    ans = ""
    stack = []
    for l in prefix:
        if l.isdigit():
            ans += l
        else:
            if "+":
                while stack and stack[-1] == "*":  # 우선순위가 높은 것을 pop
                    ans += stack.pop()
                stack.append(l)
            elif "*":  # 우선순위가 높은 연산자가 없으므로 그대로 append
                stack.append(l)

    while stack:  # 남은 연산자 추가
        ans += stack.pop()

    return ans