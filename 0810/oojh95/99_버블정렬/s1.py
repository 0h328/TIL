

def bubble_sort(N, numbers):
        for i in range(N-1, 0, -1):    # 초기는 끝이 N-1, 끝은 i가 0일때까지 -1씩해가면서 줄여간다.
            for j in range(i):  # 0의 위치에서 정해진 한도인 i범위까지 조건을 충족시키면 자리를 바꾼다.
                if numbers[j] > numbers[j+1] :
                    numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
        return numbers



import sys
sys.stdin = open('input.txt')   #입력부분
N = int(input())
numbers = list(map(int, input().split()))

print(bubble_sort(N, numbers))  #출력부분