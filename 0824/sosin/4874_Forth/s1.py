# https://swexpertacademy.com/main/learn/course/subjectDetail.do?courseId=AVuPDN86AAXw5UW6&subjectId=AWOVIc7KqfQDFAWg#

import sys
sys.stdin = open('input.txt')

for T in range(int(input())):
    nums = []
    try:
        for s in input().split():
            if s == '+':
                nums.append(nums.pop() + nums.pop())
            elif s == '*':
                nums.append(nums.pop() * nums.pop())
            elif s == '/':
                a = nums.pop()
                b = nums.pop()
                nums.append(b // a)
            elif s == '-':
                a = nums.pop()
                b = nums.pop()
                nums.append(b - a)
            elif s == '.':
                if len(nums) > 1:
                    error
                result = nums.pop()
            else:
                nums.append(int(s))
    except:
        result = 'error'

    print('#{} {}'.format((T+1), result))

#1 84
#2 error
#3 168
