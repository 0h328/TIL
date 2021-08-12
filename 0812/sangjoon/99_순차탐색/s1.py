import pathlib, sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")


def ordered_sequential_search(numbers, target):
    for num in numbers:
        if target == num:
            return True

        if target > num:
            return False
    return False

    # if target in numbers:
    #     return True
    # return False


numbers = list(map(int, input().split()))
print(ordered_sequential_search(numbers, -9))  # True
print(ordered_sequential_search(numbers, 94))  # False
