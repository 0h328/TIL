# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVF-WqqecDFAWg#
import sys
sys.stdin = open('input.txt')
for T in range(int(input())):
    blue = []
    red = []
    result = 0
    for _ in range(int(input())):
        x1, y1, x2, y2, c = map(int, input().split())
        if c == 1:
            red.append((x1, x2+1, y1, y2+1))
        else:
            blue.append((x1, x2+1, y1, y2+1))

    for b_x1, b_x2, b_y1, b_y2 in blue:
        for r_x1, r_x2, r_y1, r_y2 in red:
            w = min(b_x2, r_x2) - max(r_x1, b_x1)
            h = min(b_y2, r_y2) - max(r_y1, b_y1)
            if w > 0 and h > 0:
                result += w * h


    print('#{} {}'.format((T+1), result))

#1 4
#2 5
#3 7
