import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def is_palindrome(letter):  # 회문 판별
    letter, mid = list(letter), len(letter) // 2
    left = letter[:mid]
    right = list(reversed(letter))[:mid]

    if left == right:
        return True

    return False


test_case = int(input())

for test in range(1, test_case + 1):
    n, m = map(int, input().split())
    lst = [input() for _ in range(n)]
    ans = ""

    for i in range(n):

        for j in range(n - m + 1):
            letter = lst[i][j : j + m]
            if is_palindrome(letter):
                ans = letter

    reversed_lst = list(map(list, zip(*lst)))

    for i in range(n):
        for j in range(n - m + 1):
            letter = reversed_lst[i][j : j + m]
            if is_palindrome(letter):
                ans = "".join(letter)

    print("#{} {}".format(test, ans))