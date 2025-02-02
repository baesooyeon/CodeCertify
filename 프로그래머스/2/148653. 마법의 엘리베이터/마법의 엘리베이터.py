# 틀림 ㅠ
def solution(storey):
    storey = str(storey)

    answer = 0
    flag = False
    for idx in range(len(storey)-1, -1, -1):
        x = int(storey[idx])
        # 만약 +1이 된다면
        if flag:
            x +=1

        # 만약 x가 5가 넘는다면?
        if x>5:
            temp = 10-x
            flag = True
        elif x<5:
            temp = x
            flag = False
        elif x==5:
            temp = x
            if idx!=0:
                # 4이하라면? > 올림을 하지 않는게 좋다!
                if int(storey[idx-1])<=4:
                    flag = False
                # 5이상이라면? > 올림을 하는게 좋다!
                else:
                    flag = True
            else:
                flag = False
        answer += temp
       
    # 이거 넣으니까 정답률 46>77로 올라감
    if flag:
        answer+=1
    return answer