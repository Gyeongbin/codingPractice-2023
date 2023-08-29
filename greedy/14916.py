import sys
input = sys.stdin.readline

n = int(input().rstrip())
max_five_won = int(n / 5)
result = 0

if (max_five_won==0) :
    if(n%2==0) : result = int(n/2)
    else : result = -1

else : 
    for i in range(max_five_won+1) :
        cal = max_five_won - i
        if ((n - cal * 5) % 2 == 0) :
            two_won = int((n - cal * 5) / 2)
            result = cal + two_won
            break
        else :
            result = -1

print(result)