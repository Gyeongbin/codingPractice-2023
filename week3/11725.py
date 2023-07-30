#코드참고
#출처 : https://campkim.tistory.com/13

import sys
from collections import deque

N = int(sys.stdin.readline().rstrip())
visited = [False] * (N+1)
answer = [0] * (N+1)
E = [[] for _ in range(N+1)]

for _ in range(N-1):
    a,b = map(int, sys.stdin.readline().split())
    E[a].append(b)
    E[b].append(a)

def bfs(E, v, visited) :
    deq = deque([v])
    visited[v] = True
    while(deq):
        x = deq.popleft()
        for i in E[x]:
            if not visited[i]:
                answer[i] = x
                deq.append(i)
                visited[i] = True

bfs(E, 1, visited)

for i in range(2, N+1):
    print(answer[i])