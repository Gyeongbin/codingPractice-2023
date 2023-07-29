import sys
from heapq import heappush, heappop

heap = []

N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())
    if (num == 0) and (len(heap)==0) :
        print(0)
    elif (num == 0) :
        print(heappop(heap)[1])
    else :
        heappush(heap, (-num, num))