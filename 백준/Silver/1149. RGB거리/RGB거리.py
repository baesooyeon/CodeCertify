import sys
input = sys.stdin.readline

n = int(input())
house = [[int(i) for i in input().split()] for _ in range(n)]
dp = [[0]*3 for _ in range(n)]

for idx in range(n):
    if idx ==0:
        dp[idx] = house[idx]
    else:
        dp[idx][0] = min(dp[idx-1][1], dp[idx-1][2]) + house[idx][0]
        dp[idx][1] = min(dp[idx-1][0], dp[idx-1][2]) + house[idx][1]
        dp[idx][2] = min(dp[idx-1][0], dp[idx-1][1]) + house[idx][2]

print(min(dp[-1]))