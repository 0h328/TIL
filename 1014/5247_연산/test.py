print(bin(7))
print(bin(15))
print(bin(1007))
M = 16
M //= 2
print(M)

A = [1, 2]
B = [1, 2, 3]

if A in B:
    print('A in B')
else:
    print('this cannot')

A = {1, 2}
B = {1, 2, 3}
# print(B-A
print(A-B)

from collections import deque

queue = deque([(1, 0)])
queue.append((2,0))
print(queue)