#2.
def solve(word):
    if word == word[::-1]:  # 회문인 경우 바로 종료
        return word
    elif len(word) < 2:     # 한 글자인 경우 바로 종료
        return word
    ans = ''
    for i in range(len(word)-1):
        # key -> https://docs.python.org/3/whatsnew/2.5.html#other-language-changes
        # max의 인자의 값에서 길이(len)가 최대인 값을 반환
        ans = max(ans, palindrome(word, i, i+1), palindrome(word, i, i+2), key=len)
    return ans

def palindrome(word, left, right):
    # 포인터가 양 끝의 범위를 넘지 않으며 회문인 경우
    while left >= 0 and right < len(word) and word[left] == word[right]:
        # 포인터를 바깥으로 뻗어나가자
        left -= 1
        right += 1
    return word[left+1:right]

import sys
sys.stdin = open('input.txt')
for _ in range(1, 11):
    tc = input()
    data = [input() for _ in range(100)]
    rotated_data = [''.join(i) for i in zip(*data)]
    ans = 0

    for i in range(100):
        max_val = max(len(solve(data[i])), len(solve(rotated_data[i])))
        if max_val > ans:
            ans = max_val
    print('#{} {}'.format(tc, ans))