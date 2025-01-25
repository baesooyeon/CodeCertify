n, x = map(int, input().split())
visitors = list(map(int, input().split()))

# 누적합을 이용한다.
cum_list = [0]*len(visitors)
cum_list[0]=visitors[0]

for idx in range(1, len(visitors)):
    cum_list[idx] =cum_list[idx-1]+visitors[idx]
    
sub_cum = [0]*len(visitors)
for i in range(x-1, len(visitors)):
    if i==x-1:
        sub_cum[i] = cum_list[i]
    else:
        sub_cum[i] = cum_list[i]-cum_list[i-x]
        
max_sub_cum = max(sub_cum)
if max_sub_cum ==0:
    print("SAD")
else:
    print(max(sub_cum))
    print(sub_cum.count(max(sub_cum)))