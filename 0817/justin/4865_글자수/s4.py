import sys
sys.stdin = open('input.txt')
T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()
    my_dict = {}

    """
    fromkeys() -> https://docs.python.org/3/library/stdtypes.html#dict.fromkeys
    첫 번째 인자로 key를 만들고 두 번째 인자는 안넣으면 None이 기본
    """
    count_char = my_dict.fromkeys(str1, 0)
    for char in str2:
        if char in count_char:
            count_char[char] += 1

    ans = 0
    for val in count_char.values():
        if val > ans:
            ans = val

    print('#{} {}'.format(tc, ans))