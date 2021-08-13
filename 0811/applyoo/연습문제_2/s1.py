import sys
sys.stdin = open('input.txt')

N = int(input())
arr = [list(map(int ,input().split())) for _ in range(N)]

xy = [(-1, 0), (1, 0), (0, 1), (0, -1)]

for i, j in xy:
    print(arr[1+i][1+j])

sys.stdin = open('input2.txt')

for i, j in xy:
    print(arr[1+i][1+j])

sys.stdin = open('input2.txt')

def myFunction():
    result = 0
    for x in range(N):
        for y in range(N):
            for dx, dy in xy:
                if x+dx in range(5) and y+dy in range(5):
                    result += abs(arr[x][y] - arr[x+dx][y+dy])
    return result

T = int(input())
xy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
for test in range(T):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    print(myFunction())

# def myFunction():
#     result = 0
#     for x in range(N):
#         for y in range(N):
#             for dx, dy in xy:
#                 try:
#                     result += abs(arr[x][y] - arr[x+dx][y+dy])
#                 except:
#                     print(x+dx, y+dy)
#     return result
#
# T = int(input())
# xy = [(-1, 0), (0, 1), (1, 0), (0, -1)]
# for test in range(T):
#     N = int(input())
#     arr = [list(map(int, input().split())) for _ in range(N)]
#     print(myFunction())