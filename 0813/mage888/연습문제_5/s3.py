# 방법 3 - .find() 활용

import sys
sys.stdin = open('input.txt')

target = input()
N = len(target)

pattern = input()
M = len(pattern)

print(target.find(pattern)) # 2