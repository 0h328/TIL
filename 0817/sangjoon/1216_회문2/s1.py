import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def is_palindrome(letter: str):  # 회문 판별
    reversed_letter = letter[::-1]

    if letter == reversed_letter:
        return True

    return False


def get_palindrome(m: int):  # 문자 길이 별 회문 판별

    reversed_lst = list(map(list, zip(*lst)))

    for i in range(n):
        for j in range(n - m + 1):
            left_right_letter = lst[i][j : j + m]
            top_down_letter = reversed_lst[i][j : j + m]
            if is_palindrome(left_right_letter) or is_palindrome(top_down_letter):
                return m

    return 0


test_case = 10

for test in range(1, test_case + 1):
    test = int(input())
    lst = [input() for _ in range(100)]
    n, ans = 100, 0

    for i in range(n, 0, -1):  # 최대길이부터 회문 판별
        ans = get_palindrome(i)
        if ans:
            break

    print("#{} {}".format(test, ans))