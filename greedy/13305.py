import sys
input = sys.stdin.readline

N = int(input().rstrip())
road = list(map(int,input().split()))
value = list(map(int,input().split()))

cost = value[0]
total_cost = road[0] * cost
for i in range(1, N-1) :
    if value[i] < cost :
        cost = value[i]
        total_cost += (road[i] * cost)
    else :
        total_cost += (road[i]* cost)

print(total_cost)