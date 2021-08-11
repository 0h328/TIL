import sys
sys.stdin = open('input.txt')                   #input을 txt로 불러옴

numbers = list(map(int, input().split()))       #numbers를 하나의 list로 받아옴

def bubblesort(numbers):                        #bubblesort 함수 구현 시작
    for idx in range(len(numbers)-1, 0, -1):    #리스트의 가장 오른쪽 부분까지 검색 구간으로 설정함, 한번의 for문 진행마다 가장 오른쪽 칸 자르고 실행
        for i in range(0, idx):                 #처음 숫자부터 오른쪽 칸과 비교함, 한번의 for문 진행마다 두번째 칸으로 넘어감, idx는 range 특성을 통해 범위를 넘어가지 않게 설정
            if numbers[i] > numbers[i+1]:       #왼쪽 칸이 더 크면 오른쪽이랑 자리바꿈,
                numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
    return numbers

print(BubbleSort(numbers))