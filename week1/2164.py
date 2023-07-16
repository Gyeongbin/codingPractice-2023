from collections import deque

N = int(input())
deq = deque([i + 1 for i in range(N)])

while(len(deq)>1) :
    deq.popleft()
    deq.rotate(-1)

print(deq[0])