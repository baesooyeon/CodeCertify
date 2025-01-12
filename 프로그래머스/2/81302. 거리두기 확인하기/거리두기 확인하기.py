# places[0]만 확인하기
def solution(places):
    result = []
    for place in places:
        tmp = [[i for i in j] for j in place]
        flag = True

        for r in range(5):
            for c in range(5):
                if tmp[r][c]=="P":
                    if c+1<5 and tmp[r][c+1]!="X":
                        if (c+2<5 and tmp[r][c+2]=="P"):
                            result.append(0)
                            flag = False
                            break

                    if r+1<5 and tmp[r+1][c]!="X":
                        if (r+2<5 and tmp[r+2][c]=="P"):
                            result.append(0)
                            flag = False
                            break
                    
                    if (r+1<5 and tmp[r+1][c]=="P") or (c+1<5 and tmp[r][c+1]=="P"):
                        result.append(0)
                        flag = False
                        break
                        
                    if r+1<5 and c+1<5:
                        if tmp[r+1][c]=="O" or tmp[r][c+1]=="O":
                            if tmp[r+1][c+1]=="P":
                                result.append(0)
                                flag = False
                                break
                    
                    if r+1<5 and c-1>=0:
                        if tmp[r+1][c]=="O" or tmp[r][c-1]=="O":
                            if tmp[r+1][c-1]=="P":
                                result.append(0)
                                flag = False
                                break
                        
            if flag==False:
                break

        if flag:
            result.append(1)
            
    return result