def solution(numbers):
    str_numbers = [str(number) for number in numbers]
    str_numbers.sort(key=lambda x: x * 3, reverse=True)

    if str_numbers[0] != '0':
        answer = ''.join(str_numbers)
        return answer
    else:
        return '0'

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))