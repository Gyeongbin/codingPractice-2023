import sys
import heapq

heap = []
N = int(sys.stdin.readline().rstrip())

for _ in range(N):
    numbers = map(int,sys.stdin.readline().split())
    for number in numbers:
        if len(heap) < N: # heap의 크기를 n개로 유지
            heapq.heappush(heap, number)
        else:
            if heap[0] < number:
                heapq.heappop(heap)
                heapq.heappush(heap, number)
print(heap[0])