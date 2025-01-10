# 효율성 어떻게 해야하지..?! 
def solution(board, skill):
    tmp = [[0]*(len(board[0])+1) for _ in range(len(board)+1)]

    for type_, r1, c1, r2, c2, degree in skill:
        if type_==2:
            tmp[r1][c1]+=degree
            tmp[r1][c2+1]-=degree
            tmp[r2+1][c1]-=degree
            tmp[r2+1][c2+1]+=degree
        else:
            tmp[r1][c1]-=degree
            tmp[r1][c2+1]+=degree
            tmp[r2+1][c1]+=degree
            tmp[r2+1][c2+1]-=degree


    # 행 계산
    for i in range(len(tmp)):
        for j in range(1, len(tmp[0])):
            tmp[i][j] +=tmp[i][j-1]

    # 열 계산
    for i in range(1, len(tmp)):
        for j in range(len(tmp[0])):
            tmp[i][j]+=tmp[i-1][j]

    answer = 0
    # board와 합쳐주기
    for r in range(len(board)):
        for c in range(len(board[0])):
            board[r][c]+=tmp[r][c]
            if board[r][c]>=1:
                answer+=1

    return answer