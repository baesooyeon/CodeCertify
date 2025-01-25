import math
n = int(input())
m = int(input())
bridge = list(map(int, input().split()))

# 가장 앞쪽과 끝쪽에 대해 1
max_bridge = max(bridge[0], n-bridge[-1])

for idx in range(1, len(bridge)):
    length = math.ceil((bridge[idx]-bridge[idx-1])/2)
#     print(length)
    max_bridge = max(max_bridge, length)
    
print(max_bridge)