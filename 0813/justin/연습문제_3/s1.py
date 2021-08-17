# 문제 설계: 10분
# 문제 풀이: 40분
# 디버깅: 20분(정답 x)

def solve(word):
    global reversed_str
    if not word:  # base case -> 빈 문자열
        return word

    # print(word[-1])
    reversed_str += word[-1]  # 단어의 마지막 문자을 붙여감
    return word[-1] + solve(word[:-1])  # 마지막 직전까지 값을 인자로 넘기며 재귀적으로 호출


import sys

sys.stdin = open('input.txt')

reversed_str = ''
word1 = input()

print(solve(word1))
print(reversed_str)

print('---------------------')
word2 = input()
print(solve(word2))