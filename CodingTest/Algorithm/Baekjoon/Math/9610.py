import sys
sys.stdin = open('input.txt')

Q1 = 0
Q2 = 0
Q3 = 0
Q4 = 0
AXIS = 0
n = int(input())
for _ in range(n):
    x, y = map(int, input().split())
    if x == 0 or y == 0:
        AXIS += 1
    elif x > 0 and y > 0:
        Q1 += 1
    elif x < 0 and y > 0:
        Q2 += 1
    elif x < 0 and y < 0:
        Q3 += 1
    elif x > 0 and y < 0:
        Q4 += 1

# print('Q1: ' + str(Q1))
# print('Q2: ' + str(Q2))
# print('Q3: ' + str(Q3))
# print('Q4: ' + str(Q4))
# print('AXIS: ' + str(AXIS))

# print("Q1:", Q1)
# print("Q2:", Q2)
# print("Q3:", Q3)
# print("Q4:", Q4)
# print("AXIS:", AXIS)

print("Q1: %d" %(Q1))
print("Q2: %d" %(Q2))
print("Q3: %d" %(Q3))
print("Q4: %d" %(Q4))
print("AXIS: %d" %(AXIS))