import sys
sys.stdin = open('input.txt')

for case in range(10):
    length, data = map(int, input().split())
    data_to_str = str(data)
    stack = []
    for i in data_to_str:
        if i not in stack:
            stack.append(i)
        elif len(stack) > 0 and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    print('#{} {}'.format(case + 1, int(''.join(stack))))

