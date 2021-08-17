import sys
sys.stdin = open('input.txt')


def is_palindrome(lst):
    for str_idx in range(len(lst) // 2):
        if lst[str_idx] != lst[-1-str_idx]:
            return False
    return True


def take_out_palindrome(grid):
    ans = []
    for idx in range(N):
        for letter_idx in range(N-M+1):
            string_to_check = grid[idx][letter_idx:letter_idx + M]
            if is_palindrome(string_to_check):
                ans = string_to_check
    return ans


T = int(input())

i = 1
while i <= T:
    N, M = map(int, input().split())
    letter_grid = [list(input()) for _ in range(N)]
    letter_grid_tp = list(zip(*letter_grid))
    # print(letter_grid)

    final_palindrome = take_out_palindrome(letter_grid)
    if not final_palindrome:
        final_palindrome = take_out_palindrome(letter_grid_tp)

    print('#{0} {1}'.format(i, ''.join(final_palindrome)))
    # break
    i += 1
