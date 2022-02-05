import sys
sys.stdin = open('input.txt')

N = int(input())
tree = sorted(tuple(map(int, sys.stdin.readline().split())), reverse=True)

for i in range(N):
    tree[i] += i+1  # 심는 일 수 + 자라는 일 수

print(max(tree)+1)  # 그 다음날오므로 +1