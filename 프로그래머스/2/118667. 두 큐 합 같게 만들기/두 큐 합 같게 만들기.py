from collections import deque
def solution(queue1, queue2):

    q1 = deque(queue1)
    q2 = deque(queue2)

    sum1 = sum(q1)
    sum2 = sum(q2)
    
    limit = len(q1)*3
    
    cnt = 0
    
    while sum1!=sum2:
        if sum1>sum2:
            x = q1.popleft()
            q2.append(x)
            sum1-=x
            sum2+=x

        elif sum1< sum2:
            x = q2.popleft()
            q1.append(x)
            sum1+=x
            sum2-=x
            
        cnt+=1
        if cnt==limit:
            return -1
    return cnt