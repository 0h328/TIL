# 문제 푼 시간
# 풀이법: heap 정렬
import pathlib
import sys

sys.stdin = open(str(pathlib.Path(__file__).parent.absolute()) + "/input.txt")

test_case = int(input())


class Heap:
    def __init__(self, n: int):
        self.heap = [0] * (n+1)
        self.heap_count = 0

    def heap_push(self, value):
        self.heap_count += 1
        self.heap[self.heap_count] = value
        child = self.heap_count
        parent = child // 2

        while parent and self.heap[parent] > self.heap[child]:
            # 자식 <-> 부모 교환
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            child = parent
            parent = child // 2

    def heap_pop(self):
        return_value = self.heap[1]
        self.heap[1] = self.heap[self.heap_count]  #
        self.heap[self.heap_count] = 0
        self.heap_count -= 1

        parent = 1
        child = parent * 2

        if child + 1 <= self.heap_count:
            if self.heap[child] > self.heap[child+1]:
                child = child + 1

        while child <= self.heap_count and self.heap[parent] > self.heap[child]:
            self.heap[parent], self.heap[child] = self.heap[child], self.heap[parent]
            parent = child
            child = parent * 2

            if child + 1 <= self.heap_count:
                if self.heap[child] > self.heap[child+1]:
                    child = child + 1

        return return_value


for test in range(1, test_case + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    heap = Heap(n)
    for v in lst:
        heap.heap_push(v)

    ans = 0
    idx = n
    while idx:
        idx //= 2
        ans += heap.heap[idx]

    print("#{} {}".format(test, ans))
