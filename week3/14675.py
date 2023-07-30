import sys
input = sys.stdin.readline

N = int(input().rstrip())
vertex =[[] for _ in range(N+1)]
bridge = []

for _ in range(N-1):
    a, b = map(int, input().split())
    vertex[a].append(b)
    vertex[b].append(a)
    bridge.append([a,b])

q = int(input().rstrip())
for _ in range(q):
    isVertex, num = map(int, input().split())
    if (isVertex==1):
        if len(vertex[num]) == 1 : print('no')
        else : print('yes')
    else :
        print('yes')