# 기존에 풀어보았던 문제에서 word[1:-1] 슬라이싱 후 계속 줄여서 재귀후에 결과값을 출력하는 방법밖에 떠올르지 않아서
# 아래처럼 간단한 재귀함수를 생각하지 못했다.
# 연습문제 2번 풀이가 나는 좋다.

def solve(word):
   if len(word) == 1:
       return word

   else:
       return solve(word[1:]) + word[0]

import sys
sys.stdin = open('input.txt')

word1 = input()
word2 = input()

print(solve(word1)) # otamot
print(solve(word2)) # ananab