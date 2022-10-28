import sys
sys.stdin = open('input.txt')

# int(input(), 2) => 11001100을 10진수로 변환
# oct(int(input() ,2)) 11001100dl 10진수로 변환된 것을 8진수로 변환
# 8진수 앞에 0c를 제외한 값을 출력
print(oct(int(input(), 2))[2:])
