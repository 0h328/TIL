import sys
sys.stdin = open('input.txt')


s = list(map(str, sys.stdin.readline().rstrip("\n")))
tmp = set()             # set 자료 구조를 통해 중복을 제거


for i in range(len(s)):
    for j in range(len(s) + 1):
        if s[i:j]:
            tmp.add("".join(s[i:j]))


print(len(tmp))