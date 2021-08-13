import sys
sys.stdin = open('input.txt')

T = int(input())

for t in range(1, T+1):
     arr = [[0] * 10 for _ in range(10)]
     line = int(input())
     for l in range(line):
          order = list(map(int, input().split()))
          row1, row2 = order[0], order[2]
          col1, col2 = order[1], order[3]
          color = order[4]
          for i in range(row1, row2 + 1):
              for j in range(col1, col2 + 1):
                   arr[i][j] += color
     cnt = 0
     for i in range(10):
          for j in range(10):
               if arr[i][j] == 3:
                    cnt += 1

     print('#{} {}'.format(t, cnt))