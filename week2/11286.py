import sys
from heapq import heappop, heappush

heap = []
N = int(sys.stdin.readline().rstrip())
for _ in range(N):
    num = int(sys.stdin.readline().rstrip())  
    if (num == 0) :
        if (len(heap)==0) :
            print(0)
        else :
            print(heappop(heap)[1])
    else :
        heappush(heap, (abs(num), num))