import sys
sys.stdin = open('input.txt')

words = input().split('-')  # -를 기준으로 리스트로 나누면 됨.

ans = ''
for word in words:
    ans += word[0]  # 첫번째 인덱스만을 사용하여 출력하면 됨.

print(ans)