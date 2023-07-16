from collections import deque

inputText = input().split()
n, k = inputText

array =[]
for i in range(int(n)) :
    array.append(i+1)

deq = deque(array)
result = []


for j in range(int(n)):
    if (len(deq) <= int(k)) :
        if (len(deq)==0) : break
        else:
            for x in range(int(k)-1) :
                deq.rotate(-1)
            result.append(deq.popleft())
    else : 
        deq.rotate(-(int(k)-1))
        result.append(deq.popleft())

print('<' + ', '.join(map(str, result)) + '>')