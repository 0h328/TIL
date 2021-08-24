import sys
sys.stdin = open('input.txt')

my_list = list(map(int, input().split()))

def find_num(my_list, num):
    start = 0
    end = len(my_list) - 1
    while start <= end:
        middle = (start + end) // 2
        if num == middle:
            return True
        elif num > middle:
            start = middle + 1
        else:
            end = middle - 1
    return False

print(find_num(my_list, 3))
