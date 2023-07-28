import sys
from collections import deque

N = int(input())
deq = deque(list(map(int,sys.stdin.readline().split())))
indexs = deque([num+1 for num in range (N)])

result = []

while(1):
    if (len(indexs)==1) :
        popIndex = indexs.popleft()
        result.append(popIndex)
        break
    else: 
        count = deq.popleft()
        popIndex = indexs.popleft()
        result.append(popIndex)

        if count>0:
            deq.rotate(-(count-1))
            indexs.rotate(-(count-1))
        else:
            deq.rotate(-count)
            indexs.rotate(-count)

print(' '.join(map(str,result)))