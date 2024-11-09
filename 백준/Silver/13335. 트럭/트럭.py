from collections import deque
import sys

input = sys.stdin.readline

n, w, l = map(int, input().split())
truck = [int(i) for i in input().split()]

bridge = deque([0]*w)

idx = 0
cnt = 0
while idx <len(truck):
    if idx ==0:
        bridge.popleft()
        bridge.append(truck[idx])
        idx+=1
        cnt+=1
    else:
        # bridge가 가득차지 않고 최대 하중 이하인가?
        if len(bridge)<=w and sum(bridge)+truck[idx]-bridge[0]<=l:
            # 왼쪽에서 빼내기
            bridge.popleft()
            # 오른쪽에서 집어넣기
            bridge.append(truck[idx])
            cnt+=1
            idx+=1
            
        # 만약 만족시키지 못한다면?
        else:
            bridge.popleft()
            bridge.append(0)
            cnt+=1
            
if bridge!=deque([0]*w):
    while bridge!=deque([0]*w):
        bridge.popleft()
        bridge.append(0)
        cnt+=1
        
print(cnt)