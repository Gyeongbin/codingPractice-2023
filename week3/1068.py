import sys
input = sys.stdin.readline

def dfs(delNum, nodes) :
    nodes[delNum] = -2
    for i in range(len(nodes)) :
        if delNum == nodes[i] :
            dfs(i, nodes)

N = int(input().rstrip())
nodes = list(map(int, input().split()))
delNum = int(input().rstrip())
ct = 0

dfs(delNum, nodes)
for i in range(len(nodes)):
    if nodes[i] != -2 and i not in nodes :
        ct+=1

print(ct)