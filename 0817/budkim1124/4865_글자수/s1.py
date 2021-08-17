import sys
sys.stdin = open('input.txt')

T = int(input())

for num in range(T):
    words1 = input()
    words2 = input()
    cnt = 0
    arr = []

    for word1 in words1:
        arr.append(words2.count(word1))
    print("#{} {}".format(num+1, max(arr)))
