n = int(input())
balls = [i for i in input()]

def move_balls(balls, color):
    idx = 1
    cnt = 0

    while idx!=len(balls):    
        if balls[idx] == color:

            # 만약 양 옆의 공의 색이 다르다면
            if balls[idx]!= balls[idx-1]:
                temp_idx = idx
                while True:
                    balls1 = balls[temp_idx-1]
                    balls2 = balls[temp_idx]

                    balls[temp_idx]=balls1
                    balls[temp_idx-1] = balls2

                    if temp_idx-1==0 or balls[temp_idx-1] == balls[temp_idx-2]:
                        cnt+=1
                        # print(balls, idx)
                        break
                    temp_idx-=1

                idx+=1
            # 만약 양 옆의 공의 색이 같다면
            else:
                idx+=1
        else: idx+=1
    return cnt


newballs = balls[:]
r_balls = move_balls(newballs, "R")

newballs = balls[:]
b_balls = move_balls(newballs, "B")

newballs = balls[:]
newballs.reverse()
r_reverse_balls = move_balls(newballs, "R")

newballs = balls[:]
newballs.reverse()
b_reverse_balls = move_balls(newballs, "B")

min_move = min([r_balls, b_balls, r_reverse_balls, b_reverse_balls])

print(min_move)