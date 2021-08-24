import sys
sys.stdin = open('input.txt')

tc = int(input())
for n in range(1, tc+1):
    P, A, B = map(int, input().split())
    students = [A,B]
    result = []
    for student in students:
        cnt = 0
        start = 1
        end = P
        while start < end:
            middle = (start + end) // 2
            if middle == student:
                cnt += 1
                result.append(cnt)
                break
            elif middle > student:
                end = middle
                cnt += 1
            elif middle < student:
                start = middle
                cnt += 1
    print(result)
    if result[0] < result[1]:
        print('#{0} {1}'.format(n, 'A'))
    elif result[0] > result[1]:
        print('#{0} {1}'.format(n, 'B'))
    else:
        print('#{0} {1}'.format(n, 0))
