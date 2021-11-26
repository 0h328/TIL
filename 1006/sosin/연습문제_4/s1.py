
# 전위 순회 (V -> L -> R)
def pre_order(node):
    pass

# 중위 순회 (L -> V -> R)
def in_order(node):
    pass

# 후위 순회 (L -> R -> V)
def post_order(node):
    pass


import sys
sys.stdin = open('input.txt')

print('전위 순회 : ', end='')
pre_order(1)
print()

print('중위 순회 : ', end='')
in_order(1)
print()

print('후위 순회 : ', end='')
post_order(1)
print()