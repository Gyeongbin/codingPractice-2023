import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

N, R = map(int, input().split())
tree = [[] for _ in range(N+1)]
for _ in range(N-1):
    a, b, d = map(int, input().split())
    tree[a].append((b,d))
    tree[b].append((a,d))

ans =[0,0]

def dfs(u,p,sum,flag):
    if flag == 0: ans[0] = sum # 기가 노드까지의 간선 길이의 합
    else: ans[1] = max(ans[1],sum) # 긴 가지의 길이
    # root가 아닌데 인접노드가 2개보다 많으면, 자식이 두개 -> giga 
    # root인데 인접 노드가 2개 이상이면 ->  giga
    if flag==0 and len(tree[u]) > 2 -int(u==R): 
        flag,sum = 1, 0
    for v,w in tree[u]:
        if v== p: continue
        dfs(v,u,sum+w,flag)

dfs(R,R,0,0)
print(ans[0], ans[1])
