import sys
sys.stdin = open('input.txt')

plates = input()

height = 10
for i in range(1, len(plates)):
    if plates[i] == plates[i-1]:    # 연속되는 그릇 방향이 같으면
        height += 5                 # 높이 +5
    else:                           # 그릇 방향이 다르면
        height += 10                # 높이 +10

print(height)